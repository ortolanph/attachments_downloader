from os import path

from jinja2 import Template


class ReportManager:
    __message_index = "template/message_index.html"
    __general_index = "template/index.html"

    def generate_message_index(self, message_details, labels, attachment_details, target_folder):
        print(f"Generating report for message {message_details['message_id']}")
        with open(self.__message_index) as message_index:
            message_index_template = Template(message_index.read())

        total_size = 0

        for attachment in attachment_details:
            total_size += attachment["attachment_size"]

        total_size = total_size

        rendered_page = message_index_template.render(
            message_id=message_details["message_id"],
            message_subject=message_details["message_subject"],
            message_from=message_details["message_from"],
            message_date=message_details["message_date"],
            labels=labels,
            attachments=attachment_details,
            total_size=total_size)

        print(f"Saving file {target_folder}{path.sep}index.html")
        with open(f"{target_folder}{path.sep}index.html", 'w') as index_writer:
            index_writer.writelines(rendered_page)

        message_index.close()
        index_writer.close()
