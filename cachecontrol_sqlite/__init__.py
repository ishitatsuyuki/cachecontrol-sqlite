import sqlite3
from contextlib import contextmanager
from threading import Lock

from cachecontrol.cache import BaseCache


class SQLiteCache(BaseCache):
    def __init__(self, filename, table_name='data'):
        self.table_name = table_name
        self._connection = sqlite3.connect(filename)
        self._lock = Lock()
        with self.connection(True) as con:
            con.execute("CREATE TABLE IF NOT EXISTS `%s` (key PRIMARY KEY, value)" % self.table_name)
            con.commit()

    @contextmanager
    def connection(self, commit=False):
        with self._lock:
            yield self._connection
            if commit:
                self._connection.commit()

    def get(self, key):
        with self.connection() as con:
            val = con.execute("SELECT value FROM `%s` WHERE key=?" % self.table_name, (key,)).fetchone()
            return val[0] if val else None

    def set(self, key, value):
        with self.connection(True) as con:
            con.execute("INSERT OR REPLACE INTO `%s` VALUES (?,?)" % self.table_name, (key, value))

    def delete(self, key):
        with self.connection(True) as con:
            con.execute("DELETE FROM `%s` WHERE key=?" % self.table_name, (key,))
