# Telegram Exporter
Python script for exporting data from your telegram account

## Features:
  - Phone and code telegram authentication
  - Export your dialogs
  - Export your audios
  - Export your photos
  - Support skipping media from channels

### Usage: 
```sh
export.py --number NUMBER [--help] [--clear] [--photos] [--audios] [--full] [--include-channels]
```

### Arguments:
| Long				| Short		| Description 						|
| ----------------- | --------- | --------------------------------- |
| --help			| -h		| Show help message
| --number NUMBER	| -n NUMBER	| Telephone number
| --clear			| -c		| Clear directory before exporting
| --photos			| -p		| Export photos
| --audios			| -a		| Export audios
| --full			| -f		| Export everything
| --include-channels| -i		| Export media from channels

### Third-party libraries:
* [Telethon](https://github.com/LonamiWebs/Telethon) - Pure Python 3 MTProto API Telegram client library.
* [PySocks](https://github.com/Anorov/PySocks) - A SOCKS proxy client and wrapper for Python.
* [pyaes](https://github.com/ricmoo/pyaes) - Pure-Python implementation of AES block-cipher and common modes of operation.
* [async_generator](https://github.com/python-trio/async_generator) - Async iterators in Python 3.5.
* [pyasn1](https://github.com/etingof/pyasn1) - Generic ASN.1 library for Python.
* [rsa](https://github.com/sybrenstuvel/python-rsa/) - Python-RSA is a pure-Python RSA implementation.