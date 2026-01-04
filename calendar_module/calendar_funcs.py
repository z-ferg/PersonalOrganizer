import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def api_connect():
    SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
    creds = None

    if os.path.exists("calendar_module/token.json"):
        creds = Credentials.from_authorized_user_file("calendar_module/token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "calendar_module/credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("calendar_module/token.json", "w") as token:
            token.write(creds.to_json())
    
    try:
        service = build("calendar", "v3", credentials=creds)
        return service

    except HttpError as error:
        print(f"An error occured: {error}")
        return None

def get_all_calendars(name_only=False):
    try:
        with open('calendar/calendar_tokens.json', 'r') as file:
            data = json.load(file)
            return data.keys() if name_only else data
        
    except FileNotFoundError:
        print("Error: The file 'calendar_tokens.json' was not found")

    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON from the file: {e}")


def get_next_events(calendar, num_events=10):
    service = api_connect()
    cal_id = get_all_calendars()[calendar]

    now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
    events_result = (
        service.events()
        .list(
            calendarId=cal_id,
            timeMin=now,
            maxResults=num_events,
            singleEvents=True,
            orderBy="startTime"
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
        return []

    important_keys = ['summary', 'start', 'end', 'organizer']
    return [{key: event[key] for key in important_keys if key in event} for event in events]


if __name__ == "__main__":
    print(get_all_calendars(True))
    print(get_next_events("Virginia Tech"))