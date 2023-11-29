from src.database.message_dao import MessageDAO
from src.gmail.gmail_service import GmailService


class LabelController:
    _gmail_service = None
    _message_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._message_dao = MessageDAO()

    def insert_labels(self, message_ids, labels):
        pass