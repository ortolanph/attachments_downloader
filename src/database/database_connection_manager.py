import sqlite3


class DatabaseConnectionManager:
    _DATASOURCE = "attachments.sqlite3"
    _connection = None

    def __init__(self):
        self._connect()

    def _connect(self):
        self._connection = sqlite3.connect(self._DATASOURCE, timeout=10)

    def get_connection(self):
        return self._connection

    def reconnect(self):
        self._connect()
