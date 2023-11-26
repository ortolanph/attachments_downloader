"""
Saves or retrieves data about messages.
"""
from src.config.configuration import Configuration
from src.constants.sql_messages import (
    MESSAGE_INSERT,
    MESSAGE_LIST_ALL_IDS,
    MESSAGE_SELECT_BATCH)
from src.database.database_connection_manager import DatabaseConnectionManager


class MessageDAO:
    _connection = None
    _connection_manager = None
    _configuration = None

    def __init__(self):
        self._connection_manager = DatabaseConnectionManager()
        self._connection = self._connection_manager.get_connection()
        self._configuration = Configuration()

    def new_message(self, message_id):
        cursor = self._connection

        cursor.execute(MESSAGE_INSERT, (message_id,))

        self._connection.commit()

    def list_all_ids(self):
        cursor = self._connection.execute(MESSAGE_LIST_ALL_IDS)
        return list(map(lambda c: c[0], cursor))

    def select_messages_to_process(self):
        cursor = self._connection.execute(MESSAGE_SELECT_BATCH)
        return list(map(lambda c: c[0], cursor))
