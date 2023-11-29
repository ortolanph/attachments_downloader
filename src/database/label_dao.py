from src.config.configuration import Configuration
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
        pass

    def insert_label(self, label_id, label_name):
        pass

    def associate_with_message(self, label_id, label_message):
        pass
