"""The changelog page (changelog.html) renders CHANGELOG.md in the browser. These run its own
parser under Node with a stubbed page, so they test the code the page actually ships."""
import json
import re
import shutil
import subprocess
import unittest

from helpers import read

ORDER = ["Added", "Changed", "Fixed", "Removed", "Security", "Deprecated"]
COLOURS = {"added": "#2ecc71", "changed": "#3ba7ff", "fixed": "#ffa64d",
           "removed": "#ff4d4d", "security": "#b06bff", "deprecated": "#8a8a94"}

HARNESS = """
var md = %s, target = { innerHTML: '' };
global.document = { getElementById: function () { return target; } };
global.fetch = function () { return Promise.resolve({ ok: true, text: function () { return Promise.resolve(md); } }); };
%s
setTimeout(function () { process.stdout.write(target.innerHTML); }, 0);
"""


def parser_script():
    scripts = re.findall(r"<script>(.*?)</script>", read("changelog.html"), re.S)
    return next(s for s in scripts if "renderChangelog" in s)


@unittest.skipUnless(shutil.which("node"), "Node isn't installed")
class ChangelogPageTest(unittest.TestCase):
    def render(self, md):
        out = subprocess.run(["node"], input=HARNESS % (json.dumps(md), parser_script()),
                             capture_output=True, text=True, encoding="utf-8", check=True)
        return out.stdout

    def test_date_version_headings_are_releases(self):
        out = self.render("# Changelog\n\nIntro.\n\n## v26.10.23-1\n\n### Fixed\n\n- b\n\n"
                          "## v26.10.23\n\n### Added\n\n- a\n\n## v1.4.4\n\n### Changed\n\n- c\n")
        versions = re.findall(r'<h3 class="changelog-version">([^<]*)</h3>', out)
        self.assertEqual(["v26.10.23-1", "v26.10.23", "v1.4.4"], versions)
        self.assertNotIn("Intro.", out)

    def test_sections_are_sorted_into_the_house_order(self):
        md = "## v26.10.23\n\n" + "".join("### %s\n\n- %s item\n\n" % (s, s) for s in
                                           ["Deprecated", "Security", "Notes", "Removed", "Fixed", "Changed", "Added"])
        out = self.render(md)
        labels = re.findall(r'class="changelog-label changelog-label-([a-z]+)"', out)
        self.assertEqual([s.lower() for s in ORDER], labels)
        self.assertLess(out.index("Deprecated item"), out.index("Notes"), "unknown section types go last")

    def test_the_real_changelog_renders_every_release(self):
        md = read("CHANGELOG.md")
        out = self.render(md)
        expected = re.findall(r"^## (.+)$", md, re.M)
        self.assertEqual(expected, re.findall(r'<h3 class="changelog-version">([^<]*)</h3>', out))

    def test_page_uses_the_house_order_and_colours(self):
        page = read("changelog.html")
        self.assertIn("var CATEGORIES = [%s];" % ", ".join("'%s'" % s for s in ORDER), page)
        for name, colour in COLOURS.items():
            self.assertRegex(page, r"\.changelog-label-%s\s*\{\s*--cl:\s*%s;" % (name, re.escape(colour)))


if __name__ == "__main__":
    unittest.main()
