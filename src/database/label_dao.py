from src.config.configuration import Configuration
from src.constants.sql_labels import LABEL_EXIST, LABEL_INSERT, LABEL_ASSOCIATION_EXIST, LABEL_ASSOCIATION_INSERT
from src.database.database_connection_manager import DatabaseConnectionManager


class LabelDAO:
    _connection = None
    _connection_manager = None
    _configuration = None

    def __init__(self):
        self._connection_manager = DatabaseConnectionManager()
        self._connection = self._connection_manager.get_connection()
        self._configuration = Configuration()

    def check_label(self, label_id):
        cursor = self._connection.execute(LABEL_EXIST, (label_id,))
        return [False, True][cursor.fetchone()[0]]

    def new_label(self, label_id, label_name):
        cursor = self._connection

        cursor.execute(LABEL_INSERT, (label_id, label_name))

        self._connection.commit()

    def check_association(self, label_id, message_id):
        cursor = self._connection.execute(LABEL_ASSOCIATION_EXIST, (label_id, message_id))
        return [False, True][cursor.fetchone()[0]]

    def associate_with_message(self, label_id, message_id):
        cursor = self._connection

        cursor.execute(LABEL_ASSOCIATION_INSERT, (message_id, label_id))

        self._connection.commit()
