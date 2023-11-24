import base64
import os.path
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
ATTACHMENTS_DIR = "C:\\ortolanph\\attachments"


def login():
    print("Signing in")
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def get_messages(service, next_page_token=None):
    print("\tRetrieving messages")
    try:
        if next_page_token:
            return (service
                    .users()
                    .messages()
                    .list(userId="me",
                          q="has:attachment",
                          pageToken=next_page_token)
                    .execute())
        else:
            return (service
                    .users()
                    .messages()
                    .list(userId="me",
                          q="has:attachment")
                    .execute())
    except HttpError as error:
        print(f"Error retrieving messages: {error}")


def get_message(service, message_id):
    print("\t\tRetrieving a single message")
    try:
        return service.users().messages().get(userId="me", id=message_id).execute()
    except HttpError as error:
        print(f"Error retrieving message {message_id}: {error}")


def save_attachments(service, message, message_id):
    print("\t\t\tSaving attachment")
    try:
        for part in message["payload"]["parts"]:
            if part["filename"]:
                if 'data' in part["body"]:
                    data = part["body"]["data"]
                else:
                    att_id = part['body']['attachmentId']
                    att = (service
                           .users()
                           .messages()
                           .attachments()
                           .get(userId="me",
                                messageId=message_id,
                               id=att_id).execute()
                    )
                    data = att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))

                base_path = Path(f"{ATTACHMENTS_DIR}{os.sep}{message_id}")

                if not base_path.is_dir():
                    os.mkdir(base_path)

                path = f"{ATTACHMENTS_DIR}{os.sep}{message_id}{os.sep}{part['filename']}"
                print(f"\t\t\t\tSaving data to {path}")

                with open(path, 'wb') as f:
                    f.write(file_data)
    except HttpError as error:
        print(f"Error retrieving message {message_id}: {error}")


def main():
    try:
        service = login()

        messages = get_messages(service)
        next_page_token = messages["nextPageToken"]

        while "messages" in messages:
            for message in messages["messages"]:
                message_id = message["id"]
                my_message = get_message(service, message_id)
                save_attachments(service, my_message, message_id)

            if next_page_token:
                messages = get_messages(service, next_page_token)
                next_page_token = messages["nextPageToken"] if "nextPageToken" in messages else None
                print("\tGoing to next page")
            else:
                break

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
