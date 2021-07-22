# PancakeSwap monitor

Informs you when a new crypto currency token is available for trading on [PancakeSwap](https://pancakeswap.com/)].

## Features

- Monitors a list of crypto currency tokens available on [PancakeSwap](https://pancakeswap.com/)]
- Informs you via Telegram when a new token is available for trading
- Updates every 5 minutes (which is limited by the public [PancakeSwap API](https://github.com/pancakeswap/pancake-info-api))

## Requirements

- Python          [3.9](https://www.python.org/downloads/)
- Requests        2.25.1

## Installation

- Install Python 3.9 or higher
- Add python to your PATH (can be configured during Python installation)
- Clone the repository
- Install the requirements
```
git clone https://github.com/tmxkn1/pancake-monitor.git
cd pancake-monitor
python -m pip install -r requirements.txt
```

## Usage

- Go to the directory where the script is located
- Edit `credentials/telegram_bot.json.example`:
  - add your Telegram bot information
  - Add `chat_id` of your Telegram account or whoever is the admin
  - Add `chat_id`s of the users you want to receive notifications, including the admin if applicable
  - Save the file and remove the `.example` extension
- Run `main.py`