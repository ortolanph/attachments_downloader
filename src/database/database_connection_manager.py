import sqlite3


class DatabaseConnectionManager:
    _connection = None
    _datasource = "attachments.sqlite3"

    def __init__(self):
        self._connect()

    def _connect(self):
        self._connection = sqlite3.connect(self._datasource, timeout=10)

    def get_connection(self):
        return self._connection

    def reconnect(self):
        self._connect()
