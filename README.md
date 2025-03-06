# Download HQs Online

<p align="center">
  <br />
  <img
    src="[./_docs/assets/icon.png](https://www.google.com/imgres?q=tmnt%20image%20logo%20png&imgurl=https%3A%2F%2Fstatic.wikia.nocookie.net%2Flogocomics%2Fimages%2F1%2F1c%2FLogo-small.png%2Frevision%2Flatest%3Fcb%3D20180105040002&imgrefurl=https%3A%2F%2Flogocomics.fandom.com%2Fwiki%2FTeenage_Mutant_Ninja_Turtles&docid=52TLW-C0-NI1WM&tbnid=6cmAHFY7uiGEzM&vet=12ahUKEwiYo6TjuPaLAxUsgWEGHZtKFIoQM3oECBcQAA..i&w=400&h=326&hcb=2&ved=2ahUKEwiYo6TjuPaLAxUsgWEGHZtKFIoQM3oECBcQAA)"
    alt="Download HQs Online"
    width="150"
  />
  <br />
  <b>Download HQs Online</b>
  <br />
  <sub><sup><b>(DOWNLOAD-HQ)</b></sup></sub>
  <br />
</p>

<p align="center">
  This Python-based application automates the download of comic books (HQs) from online sources.
  It is designed to facilitate the retrieval and organization of comic files efficiently.
  <br />
</p>

<p align="center">
  Developed with Python and various modern libraries for handling web requests, file management,
  and automation, this project aims to simplify the process of downloading and structuring comic book files.
  <br />
</p>

<p align="center">
  <br />
  <img src="./_docs/assets/carbon.png" />
</p>

## Features

| Feature            | Description                                  |
|--------------------|----------------------------------------------|
| Automated Download | Fetches HQ files from predefined URLs       |
| File Organization | Renames and stores comics systematically     |
| URL Validation    | Ensures valid links before attempting download |

## Techniques Used

- **Requests:** Handles web requests for downloading HQ files.  
- **OS & Shutil:** Manages file operations and organization.  
- **Regex:** Validates URLs and file names.  

## Dependencies

| Package  | Version  | Link |
|----------|---------|------|
| Requests | Latest  | [PyPi](https://pypi.org/project/requests/) |
| OS       | Built-in | [Docs](https://docs.python.org/3/library/os.html) |
| Shutil   | Built-in | [Docs](https://docs.python.org/3/library/shutil.html) |

## 🛠️ Architecture

```bash
src
├── 📂 Scripts        # Core scripts for downloading HQs
├── 📂 Utils          # Helper functions for validation and organization
├── 📂 Configs        # Settings and parameters for execution
├── 📂 Tests          # Unit tests for the download functionality
