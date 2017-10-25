import unittest

import requests
from cachecontrol import CacheControl

from cachecontrol_sqlite import SQLiteCache


class SQLiteCacheTest(unittest.TestCase):
    def setUp(self):
        self.url = "https://httpbin.org/cache/60"
        self.sess = CacheControl(requests.Session(), cache=SQLiteCache(":memory:"))

    def tearDown(self):
        self.sess.close()

    def test_simple(self):
        response = self.sess.get(self.url)
        assert not response.from_cache
        response = self.sess.get(self.url)
        assert response.from_cache


if __name__ == '__main__':
    unittest.main()
