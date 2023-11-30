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

        for label_id in labels:
            print(f"Checking if label exists")
            exist_label = self._label_dao.check_label(label_id)

            if not exist_label:
                print(f"Creating new Label")
                if not label_id.startswith("Label_"):
                    label_name = label_id
                else:
                    label_info = self._gmail_service.get_label_info(label_id)
                    print(label_info)
                    label_name = label_info["name"]

                self._label_dao.new_label(label_id, label_name)

            print(f"Checking label association with message ({message_id} - {label_id})")
            exist_association = self._label_dao.check_association(label_id, message_id)

            if not exist_association:
                print(f"Creating new label association with message ({message_id} - {label_id})")
                self._label_dao.associate_with_message(label_id, message_id)
