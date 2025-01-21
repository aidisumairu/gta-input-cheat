import json
import time
import subprocess
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load GTA SA cheats from JSON file
with open(os.path.join(script_dir, "gta_sa_cheats.json"), "r") as file:
    gta_cheats = json.load(file)

def send_cheat_with_ahk(cheat_code):
    ahk_path = r"C:\Program Files\AutoHotkey\AutoHotkey.exe"
    script_path = os.path.join(script_dir, "send_cheat.ahk")
    try:
        subprocess.run([ahk_path, script_path, cheat_code], capture_output=True, text=True)
    except Exception as e:
        print(f"Error: {e}")

def process_chat_message(message):
    text = message["snippet"]["displayMessage"].upper()
    author_name = message["authorDetails"]["displayName"]
    if text in gta_cheats:
        cheat_code = gta_cheats[text]
        send_cheat_with_ahk(text.lower())
        print(f"Cheat executed: {cheat_code} -{author_name}")

# Scopes for YouTube Data API
SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

def authenticate_youtube():
    creds = None
    try:
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    except Exception:
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_live_chat_id(service):
    request = service.liveBroadcasts().list(
        part="snippet",
        broadcastType="all",
        broadcastStatus="active"
    )
    response = request.execute()

    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["snippet"]["liveChatId"]
    else:
        raise Exception("No live broadcast found.")

def get_live_chat_messages(service, live_chat_id, page_token=None):
    request = service.liveChatMessages().list(
        liveChatId=live_chat_id,
        part="snippet,authorDetails",
        maxResults=20,
        pageToken=page_token
    )
    return request.execute()

def main():
    creds = authenticate_youtube()
    service = build("youtube", "v3", credentials=creds)

    live_chat_id = get_live_chat_id(service)

    next_page_token = None

    while True:
        response = get_live_chat_messages(service, live_chat_id, next_page_token)
        messages = response.get("items", [])
        for message in messages:
            process_chat_message(message)
        
        next_page_token = response.get("nextPageToken", None)
        time.sleep(5)

if __name__ == "__main__":
    main()
