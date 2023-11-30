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
