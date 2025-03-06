# Download HQs Online

<p align="center">
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
