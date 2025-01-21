# GTA Input Cheat

GTA Input Cheat is a Python-based application that converts YouTube live chat inputs into keyboard inputs specifically for triggering GTA San Andreas cheats. This is a prototype, but all core functions are fully operational.

---

## Features

- Monitors YouTube live chat for user inputs.
- Filters valid GTA San Andreas cheat codes from the chat.
- Sends the cheat codes as keyboard inputs via AutoHotkey.

---

## Prerequisites

Before using the app, ensure you have the following installed and configured:

1. Python (3.7 or higher recommended).
2. AutoHotkey installed on your system: [Download AutoHotkey](https://www.autohotkey.com/).
3. Google APIs Python client library dependencies.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aidisumairu/gta-input-cheat.git
   cd gta-input-cheat
2. Install the required Python dependencies:
    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

---

## Setup
1. Obtain a client_secret.json from your Google account:

    - Go to the [Google Cloud Console](https://console.cloud.google.com/).
    - Create a project and enable the YouTube Data API.
    - Generate OAuth 2.0 client credentials and download the client_secret.json.
2. Place the client_secret.json file in the root directory of the project.

---

## Usage
1. Run the application to generate the required access token:

        python main.py

    - The app will prompt you to authenticate via your Google account.
    - A token file will be saved locally after successful authentication.
2.  Start monitoring YouTube live chat and converting inputs:

        python main.py
3. The app will automatically recognize valid GTA San Andreas cheats from the chat and send the corresponding keyboard inputs via AutoHotkey.

---

## Limitations
- This app is a prototype and may require additional testing for extended usage.
- Only inputs corresponding to GTA San Andreas cheat codes are processed.
- Requires a stable internet connection for live chat monitoring.

---

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit).

---

## Disclaimer
This application is provided as-is for prototyping purposes. The developers are not responsible for misuse or unintended consequences of using this tool.