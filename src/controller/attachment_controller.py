import base64
from os import path

from src.database.attachment_dao import AttachmentDAO
from src.gmail.gmail_service import GmailService


class AttachmentController:
    _gmail_service = None
    _attachment_dao = None

    def __init__(self):
        self._gmail_service = GmailService()
        self._attachment_dao = AttachmentDAO()

    def insert_attachments(self, message_id, attachments):
        print("Gets all the parts of the message that contains attachments")
        attachments_with_file_name = list(filter(lambda a: a["filename"] != '', attachments))

        print("Insert attachment")
        for attachment in attachments_with_file_name:
            if "attachmentId" in attachment["body"]:
                attachment_id = attachment["body"]["attachmentId"]
                exist_attachment = self._attachment_dao.check_attachment_for_message_id(message_id)

                if not exist_attachment:
                    attachment_data = self._gmail_service.get_attachment_data(message_id, attachment_id)["data"]
                    self._attachment_dao.insert_attachment(
                        attachment_id,
                        message_id,
                        attachment["filename"],
                        attachment["mimeType"],
                        attachment_data,
                        attachment["body"]["size"])

    def get_message_attachments(self, message_id):
        print(f"Fetching attachments for message {message_id}")
        return self._attachment_dao.get_message_attachment(message_id)

    def download(self, attachment, message_target_folder):
        print(f"Saving attachment {attachment['attachment_name']} to {message_target_folder}")

        file_data = base64.urlsafe_b64decode(attachment['attachment_data'].encode('UTF-8'))
        file_path = f"{message_target_folder}{path.sep}{attachment['attachment_name']}"

        with open(file_path, 'wb') as attachment_file:
            attachment_file.write(file_data)

        self._attachment_dao.update_attachment_status(attachment['attachment_id'])
