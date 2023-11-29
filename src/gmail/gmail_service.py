"""
Gmail Service
"""
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.config.configuration import Configuration


class GmailService:
    """
    Class Gmail Service
    """
    _SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
    _service = None
    _configuration = None

    _secrets_dir = "./secrets/"

    def __init__(self):
        """
        Creates a service for gmail.
        """
        self._configuration = Configuration().get_gmail_config()

        token_path = self._configuration["token"]
        credentials_path = self._configuration["credentials"]

        creds = None
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, self._SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path, self._SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open(token_path, "w") as token:
                token.write(creds.to_json())

        self._service = build(self._configuration["serviceName"], self._configuration["version"], credentials=creds)

    def service(self):
        """
        Gets the cretated service
        :return: the created service
        """
        return self._service

    def get_all_message_ids(self, next_page_token=None):
        """
        Return all the message ids
        :return: return all the message ids
        """
        messages = (self._service.users()
                    .messages()
                    .list(
                        userId=self._configuration["userId"],
                        q=self._configuration["query"],
                        pageToken=next_page_token)
                    .execute())

        ids = list(map(lambda m: m["id"], messages["messages"]))

        if "nextPageToken" in messages:
            ids.extend(self.get_all_message_ids(messages["nextPageToken"]))

        return ids

    def get_message_data(self, message_id):
        print(f"Retrieving a data for message {message_id}")
        try:
            return self._service.users().messages().get(userId="me", id=message_id).execute()
        except HttpError as error:
            print(f"Error retrieving message {message_id}: {error}")

    def get_label_info(self, label_id):
        pass
