from src.database.message_dao import MessageDAO
from src.gmail.gmail_service import GmailService
from src.utils.utils import transform_headers


class MessageController:
    _gmail_service = None
    _message_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._message_dao = MessageDAO()

    def reload_message_ids(self):
        print("Getting all database Ids")
        current_ids = self._message_dao.list_all_ids()
        print("Getting all gmail message Ids")
        message_ids = self._gmail_service.get_all_message_ids()

        print("Getting all missing Ids")
        missing_ids = list(set(message_ids) - set(current_ids))

        print("Inserting missing ids")
        for message_id in missing_ids:
            self._message_dao.new_message(message_id)
            print(f"Message id {message_id} inserted")

    def load_next_messages(self):
        print("Selecting next messages")
        return self._message_dao.select_next_messages()

    def fetch_message(self, message_id):
        print("Fetching messages to process")
        return self._gmail_service.get_message_data(message_id)

    def update_message_data(self, message_id, payload_headers):
        print("Updating message data")
        header_data = transform_headers(payload_headers)

        print("Fectching headers information")
        message_from = header_data["From"]
        message_subject = header_data["Subject"]
        message_date = header_data["Date"]

        self._message_dao.update_message_data(
            message_id,
            message_from,
            message_subject,
            message_date)

    def mark_message_as_processed(self, message_id):
        print("Marking message as processed")

        self._message_dao.mark_as_processed(message_id)

    def load_next_messages_to_download(self):
        print("Getting the next messages to download")

        return self._message_dao.select_next_processed_messages()

    def mark_message_as_downloaded(self, message_id):
        print("Marking message as downloaded")

        self._message_dao.mark_as_downloaded(message_id)

    def get_all_downloaded_messages(self):
        print("Getting all the downloaded messages")
        return self._message_dao.select_downloaded_messages()
