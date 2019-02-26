# Telegram Exporter
Python script for exporting data from your telegram account

Features:
  • Phone and code telegram authentication
  • Export your dialogs
  • Export your audios
  • Export your photos
  • Support skipping media from channels

Usage: export.py [-h] --number NUMBER
                 [--clear] [--photos]
                 [--audios] [--full]
                 [--include-channels]

Arguments:
  -h, --help                  Show this help message
  --number NUMBER, -n NUMBER  Telephone number
  --clear, -c                 Clear directory before exporting
  --photos, -p                Export photos
  --audios, -a                Export audios
  --full, -f                  Export everything
  --include-channels, -i.     Export media from channels