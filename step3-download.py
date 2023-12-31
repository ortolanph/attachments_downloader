from os import path

from src.config.configuration import Configuration
from src.report.report_manager import ReportManager
from src.utils.utils import create_target_folder
from src.controller.message_controller import MessageController
from src.controller.label_controller import LabelController
from src.controller.attachment_controller import AttachmentController

if __name__ == '__main__':
    print("Step 3 - Download message")

    configuration = Configuration()
    targetFolder = configuration.get_target_config()["folder"]

    create_target_folder(targetFolder)

    message_controller = MessageController()
    label_controller = LabelController()
    attachment_controller = AttachmentController()
    report_manager = ReportManager()

    messages = message_controller.load_next_messages_to_download()

    for message in messages:
        message_target_folder = f"{targetFolder}{path.sep}{message['message_id']}"
        create_target_folder(message_target_folder)

        labels = label_controller.get_message_labels(message['message_id'])
        attachments = attachment_controller.get_message_attachments(message['message_id'])

        report_manager.generate_message_index(
            message_details=message,
            labels=labels,
            attachment_details=attachments,
            target_folder=message_target_folder)

        for attachment in attachments:
            attachment_controller.download(attachment, message_target_folder)

        message_controller.mark_message_as_downloaded(message['message_id'])

    downloaded_messages = message_controller.get_all_downloaded_messages()
    report_manager.generate_general_index(messages=downloaded_messages, target_folder=targetFolder)
