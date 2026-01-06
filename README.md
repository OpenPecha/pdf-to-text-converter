# README

> **Note:** This readme template is based on one from the [Good Docs Project](https://thegooddocsproject.dev). You can find it and a guide to filling it out [here](https://gitlab.com/tgdp/templates/-/tree/main/readme). (_Erase this note after filling out the readme._)

<h1 align="center">
  <br>
  <a href="https://openpecha.org"><img src="https://avatars.githubusercontent.com/u/82142807?s=400&u=19e108a15566f3a1449bafb03b8dd706a72aebcd&v=4" alt="OpenPecha" width="150"></a>
  <br>
</h1>

## PDF to Text Converter (via Google Drive API)
This tool leverages Google Drive's built-in OCR and document conversion capabilities to extract text from PDFs

## Owner(s)

_Change to the owner(s) of the new repo. (This template's owners are:)_


## Table of contents
<p align="center">
  <a href="#project-description">Project description</a> •
  <a href="#who-this-project-is-for">Who this project is for</a> •
  <a href="#project-dependencies">Project dependencies</a> •
  <a href="#instructions-for-use">Instructions for use</a> •
  <a href="#contributing-guidelines">Contributing guidelines</a> •
  <a href="#additional-documentation">Additional documentation</a> •
  <a href="#how-to-get-help">How to get help</a> •
  <a href="#terms-of-use">Terms of use</a>
</p>
<hr>

## Project description
_Use one of these:_

PDF to Text Converter is a Python utility that automates the process of extracting text from ```.pdf``` files.
It uploads the PDF to Google Drive, converts it into a Google Document, and then exports the result as a ```.txt``` file.

This project helps you:

- Convert ```.pdf``` into editable ```.txt``` files.


## Who this project is for
This project is intended for user who wants to convert ```.pdf``` file to ```.txt``` file.


## Project dependencies
Before using PDF to Text Converter, ensure you have:
* python versionn >= 3.8
* A Google Cloud Platform (GCP) project with the Google Drive API enabled.
* A credential.json file (OAuth 2.0 Client ID) from your GCP project.


## Instructions for use
### Install PDF to Text Converter


1. Set up Google Cloud Credentials
    1. Go to the Google Cloud Console.
    2. Create a new project or select an existing one.
    3. Enable the Google Drive API.
    4. Navigate to APIs & Services > Credentials.
    5. Create OAuth 2.0 Client IDs (application type: Desktop App).
    6. Download the JSON file, rename it to credential.json

2. Install Dependencies
   1. Run the following command to install the required Python libraries: 

```bash
pip install google-api-python-client google-auth-oauthlib requests
```

3. Run the Converter
  - Run the main.py script and pass the path to your PDF as an argument.
```bash
python main.py path/to/your/document.pdf
```

The script will:

1. Open a browser window for you to log in to your Google account (first time only).
2. Upload file_name.pdf.
3. Create a new file named output.txt containing the extracted text.



## Contributing guidelines
If you'd like to help out, check out our [contributing guidelines](/CONTRIBUTING.md).


## How to get help
* File an issue.
* Email us at openpecha[at]gmail.com.
* Join our [discord](https://discord.com/invite/7GFpPFSTeA).


## Terms of use
PDF to Text Converter is licensed under the [MIT License](/LICENSE.md).
