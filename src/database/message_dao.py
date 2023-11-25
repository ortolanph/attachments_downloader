"""
Saves or retrieves data about messages.
"""
from src.constants.sql_messages import INSERT_MESSAGE
from src.database.database_connection_manager import DatabaseConnectionManager


class MessageDAO:
    _connection = None
    _connection_manager = None

    def __init__(self):
        self._connection_manager = DatabaseConnectionManager()
        self._connection = self._connection_manager.get_connection()

    def new_message(self, message_id):
        cursor = self._connection

        cursor.execute(INSERT_MESSAGE, (message_id,))

        self._connection.commit()
