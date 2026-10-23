<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://global.media.stux.group/logo-light.png"><source media="(prefers-color-scheme: light)" srcset="https://global.media.stux.group/logo-dark.png"><img src="https://global.media.stux.group/logo-dark.png" height="80" alt="Stux.Group Logo"></picture>
</p>

# Contributing to Maintenance Page

Maintenance Page is a [Stux.Group](https://stux.group) project — the repository
is not open to public pull requests. This document exists for anyone with
write access to the repo who wants to work on it consistently.

## Local setup

Just clone the repo and run `./dev-server.sh [port]` (or `dev-server.bat [port]`
on Windows) — starts PHP's built-in server pointed at the directory, since it's
a static site with no build step. Then open `http://127.0.0.1:8000`.

## Project conventions

- **Plain static HTML.** No framework, no build step. Barlow and Font Awesome
  are self-hosted under `assets/` (not loaded from a CDN) — if you bump the
  Font Awesome version or add font weights, update `assets/` and re-check
  which files each page actually references.
- Deployed via GitHub Pages to [maintenancepage.stux.group](https://maintenancepage.stux.group)
  (see `CNAME`) — pushing to `main` deploys automatically.
- This is a sister repo based on `soonpage`'s design — if you change shared
  styling/structure here (theme toggle, social links, legal link, animated
  background), consider whether it should change there too.
- The sitemap (`sitemap.xml`, `sitemap/index.html`, `robots.txt`) is generated: after adding or removing a page, edit the `PAGES` list in `scripts/build-sitemap.py` and run `python scripts/build-sitemap.py`, then commit the result
- The icon tags and the Discord link preview in each page's `<head>` (between the `BEGIN head tags` / `END head tags` comments) are generated: edit `scripts/build-head-tags.py` (add new pages to its `PAGES` list too) and run `python scripts/build-head-tags.py`; `build-sitemap.py` runs it for you. The icons themselves are `favicon.ico`, `apple-touch-icon.png`, `site.webmanifest` and `assets/icon-*.png`

## Tests

Run `bash tests/run.sh` before every release. It needs Python 3 and Node (and PHP 7.4 for the dev-server checks, which are skipped without it), with no other dependencies. It checks that `VERSION.md` is a valid Date Version matching the newest `CHANGELOG.md` entry, that the changelog page reads Date Version headings and orders its sections correctly, that every page's Discord preview is valid and up to date, and that the icon set is complete and served correctly.

## Versioning and changelog

- Maintenance Page uses [Date Versioning](https://datevers.ing): the version is the UTC release date as `YY.MM.DD`, plus `-1`, `-2`… for later releases the same UTC day (`26.10.23`, then `26.10.23-1`). Always take the date from `date -u`, never local time, and never use a future date. Releases up to v1.4.4 used Semantic Versioning
- The version lives in `VERSION.md` (the bare version, no `v`) — set it on every release; git tags and changelog headings keep the `v` (`v26.10.23`)
- Every release gets a `CHANGELOG.md` entry (`## vYY.MM.DD`) using `### Added` / `### Changed` / `### Fixed` / `### Removed` / `### Security` / `### Deprecated` subsections, in that order — never a bare bullet list directly under a version heading
- `commit.sh` (bash) and `commit.bat` (Windows) read `VERSION.md`, refuse a version that isn't a valid Date Version or is dated in the future (UTC), warn if it's dated before today, then handle the commit + `git tag` for a release — no need to edit them per release. They don't push; push with `git push origin main --tags`
