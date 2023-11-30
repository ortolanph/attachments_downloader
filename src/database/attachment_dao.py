from src.config.configuration import Configuration
from src.constants.sql_attachments import ATTACHMENT_EXIST, ATTACHMENT_INSERT
from src.database.database_connection_manager import DatabaseConnectionManager


class AttachmentDAO:
    _connection = None
    _connection_manager = None
    _configuration = None

    def __init__(self):
        self._connection_manager = DatabaseConnectionManager()
        self._connection = self._connection_manager.get_connection()
        self._configuration = Configuration()

    def check_attachment(self, attachment_id):
        cursor = self._connection.execute(ATTACHMENT_EXIST, (attachment_id,))
        return [False, True][cursor.fetchone()[0]]

    def insert_attachment(self, attachment_id, message_id, filaname, mime_type, attachment_data, size):
        cursor = self._connection

        cursor.execute(ATTACHMENT_INSERT, (attachment_id, message_id, filaname, mime_type, attachment_data, size))

        self._connection.commit()
