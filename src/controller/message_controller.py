from src.database.message_dao import MessageDAO
from src.gmail.gmail_service import GmailService


class MessageController:
    _gmail_service = None
    _message_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._message_dao = MessageDAO()

    def get_all_message_ids(self):
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
