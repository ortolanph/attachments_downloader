from src.database.message_dao import MessageDAO
from src.gmail.gmail_service import GmailService


class MessageController:
    _gmail_service = None
    _message_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._message_dao = MessageDAO()

    def get_all_message_ids(self):
        message_ids = self._gmail_service.get_all_message_ids()

        for message_id in message_ids:
            self._message_dao.new_message(message_id)
            print(f"Message id {message_id} inserted")
