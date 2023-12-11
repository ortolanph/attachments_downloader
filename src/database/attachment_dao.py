from src.config.configuration import Configuration
from src.constants.sql_attachments import ATTACHMENT_EXIST, ATTACHMENT_INSERT, ATTACHMENT_BY_MESSAGE_ID
from src.database.database_connection_manager import DatabaseConnectionManager


class AttachmentDAO:
    _connection = None
    _connection_manager = None
    _configuration = None

    def __init__(self):
        self._connection_manager = DatabaseConnectionManager()
        self._connection = self._connection_manager.get_connection()
        self._configuration = Configuration()

    def check_attachment_for_message_id(self, message_id):
        cursor = self._connection.execute(ATTACHMENT_EXIST, (message_id,))
        result = cursor.fetchone()[0]
        return True if result > 0 else False

    def insert_attachment(self, attachment_id, message_id, filename, mime_type, attachment_data, size):
        cursor = self._connection

        cursor.execute(ATTACHMENT_INSERT, (attachment_id, message_id, filename, mime_type, attachment_data, size))

        self._connection.commit()

    def get_message_attachment(self, message_id):
        cursor = self._connection.execute(ATTACHMENT_BY_MESSAGE_ID, (message_id,))
        return list(map(lambda c: {
            "attachment_id": c[0],
            "attachment_name": c[1],
            "attachment_type": c[2],
            "attachment_data": c[3],
            "attachment_size": c[4] / 1024}, cursor))
