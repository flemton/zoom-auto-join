# Zoom Auto Join

Automatically join scheduled Zoom meetings at specified times. Perfect for recurring meetings, classes, or standups.

## Features

- 📅 Schedule multiple recurring meetings
- 🕐 Configure specific days and times
- 🔗 Support for any meeting link (Zoom, Google Meet, Teams, etc.)
- 💾 JSON-based configuration
- 🖥️ Opens meetings in default browser
- 📜 Detailed logging

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Edit `meetings.json` to add your meetings:
```json
[
  {
    "name": "Daily Standup",
    "link": "https://zoom.us/j/123456789",
    "time": "09:00",
    "days": ["monday", "tuesday", "wednesday", "thursday", "friday"]
  }
]
```

2. Run the script:
```bash
python main.py
```

## Configuration

- `name`: Meeting name (for logging)
- `link`: Meeting URL
- `time`: Time in 24-hour format (HH:MM)
- `days`: Array of days (monday, tuesday, wednesday, thursday, friday, saturday, sunday)

## Requirements

- Python 3.7+
- schedule
- webbrowser (built-in)

## Note

Keep your computer awake during scheduled times. The script must be running to auto-join meetings.
