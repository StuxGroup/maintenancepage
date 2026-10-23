<p align="center">
  <picture><source media="(prefers-color-scheme: dark)" srcset="https://global.media.stux.group/logo-light.png"><source media="(prefers-color-scheme: light)" srcset="https://global.media.stux.group/logo-dark.png"><img src="https://global.media.stux.group/logo-dark.png" height="100" alt="Stux.Group Logo"></picture>
</p>

# Maintenance Page

A clean and simple maintenance page template for Stux.Group projects based on the soonpage design.

## Overview

This repository contains a lightweight HTML maintenance page designed to inform visitors that a service is temporarily unavailable due to updates or maintenance. It keeps your audience informed while work is underway.

## Features

- 📄 Simple, clean HTML structure
- ⚡ Lightweight and fast-loading
- 🎨 Ready to customize
- 📱 Responsive design
- 🚀 Deployed at [maintenancepage.stux.group](http://maintenancepage.stux.group/)
- 🔄 Based on the soonpage template

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/StuxGroup/maintenancepage.git
   ```

2. Open `index.html` in your browser or deploy to your hosting provider

## Customization

Edit the HTML files to:

- Update the maintenance message and expected return time
- Add your branding and logo
- Customize colors and styling
- Include contact information or status updates
- Add social media links

## Deployment

This project uses GitHub Pages and is automatically deployed to [maintenancepage.stux.group](http://maintenancepage.stux.group/).

## Versioning

Maintenance Page uses [Date Versioning](https://datevers.ing): each release is numbered by its UTC release date as `YY.MM.DD` (for example `26.10.23`), with `-1`, `-2`… added for later releases the same day. The current version is in [`VERSION.md`](VERSION.md) and every release is listed in [`CHANGELOG.md`](CHANGELOG.md) (also shown at [/changelog](https://maintenancepage.stux.group/changelog)). Releases up to v1.4.4 used Semantic Versioning.

## License

This project is open source and available for use and modification.

---

Made by [Stux.Group](https://github.com/StuxGroup)

*Stux.Group is the parent of the <picture><source media="(prefers-color-scheme: dark)" srcset="https://global.media.stux.group/icon-light.png"><source media="(prefers-color-scheme: light)" srcset="https://global.media.stux.group/icon-dark.png"><img src="https://global.media.stux.group/icon-dark.png" height="14" alt="Stux.Group" valign="middle"></picture> Stux.Group Brand of Companies.*

## Local preview

Run `./dev-server.sh` (or `dev-server.bat`, add a port as the last argument) to serve the site at `http://127.0.0.1:8000` the way GitHub Pages does, with the dev-mode banner on. Add `--no-dev-mode` to see it exactly as production does, or `?banner=soon,maintenance,site` to preview the other banner types. It uses PHP 7.4's built-in server (set `PHP_BIN` to pick another PHP).

Run the tests with `bash tests/run.sh` (Python 3 and Node; PHP 7.4 for the dev-server checks).
