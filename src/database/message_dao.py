"""
Saves or retrieves data about messages.
"""
from src.config.configuration import Configuration
from src.constants.sql_messages import (
    MESSAGE_INSERT,
    MESSAGE_LIST_ALL_IDS,
    MESSAGE_SELECT_BATCH, MESSAGE_UPDATE, MESSAGE_MARK_AS_PROCESSED, MESSAGE_SELECT_BATCH_PROCESSED)
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

    def select_next_messages(self):
        batch_size = self._configuration.get_batch_config()["size"]
        print(f"Fetching first {batch_size} messages")
        cursor = self._connection.execute(MESSAGE_SELECT_BATCH, (batch_size,))
        return list(map(lambda c: c[0], cursor))

    def select_next_processed_messages(self):
        batch_size = self._configuration.get_batch_config()["size"]
        print(f"Fetching first {batch_size} processed messages")
        cursor = self._connection.execute(MESSAGE_SELECT_BATCH_PROCESSED, (batch_size,))
        return list(map(lambda c: {
            "message_id": c[0],
            "message_from": c[1],
            "message_subject": c[2],
            "message_date": c[3]}, cursor))

    def update_message_data(self, message_id, message_from, message_subject, message_date):
        print("Updating message data")
        cursor = self._connection

        cursor.execute(MESSAGE_UPDATE, (message_from,
                                        message_subject,
                                        message_date,
                                        message_id))

        self._connection.commit()

    def mark_as_processed(self, message_id):
        print("Marking message as processed")
        cursor = self._connection

        cursor.execute(MESSAGE_MARK_AS_PROCESSED, (message_id,))

        self._connection.commit()
