from distutils.core import setup

setup(
    name='cachecontrol-sqlite',
    version='0.1.0',
    packages=['cachecontrol_sqlite'],
    url='https://github.com/ishitatsuyuki/cachecontrol-sqlite',
    license='Apache-2.0',
    author='Tatsuyuki Ishi',
    author_email='ishitatsuyuki@protonmail.com',
    description='SQLite backend for requests CacheControl',
    install_requires=['CacheControl']
)
