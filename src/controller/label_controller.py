from src.database.label_dao import LabelDAO
from src.gmail.gmail_service import GmailService


class LabelController:
    _gmail_service = None
    _label_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._label_dao = LabelDAO()

    def insert_labels(self, message_id, labels):
        print(f"Adding labels to message {message_id}")

        for label in labels:
            # 1. Verify if label is already on label table
            #    If not
            #    1.1. If label starts with "Label_",
            #       1.1.1. Call label gmail service to get label name
            #       If not, label name = label id
            # 2. Check message association
            #     2.1. If not associate, associate
            #     2.2. I associated, skip
            pass
