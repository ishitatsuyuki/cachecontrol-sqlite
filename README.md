# cachecontrol-sqlite

This is a SQLite cache backend for [CacheControl](https://github.com/ionrock/cachecontrol).

## Quickstart

```python
import requests
from cachecontrol import CacheControl
from cachecontrol_sqlite import SQLiteCache

sess = CacheControl(requests.Session(),
                    cache=SQLiteCache('cache.db'))
                    
response = sess.get("https://httpbin.org/cache/60")
```