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

- [Create a Telegram bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot) for sending messages to your users (later referred to as user_msg_bot)
- (optional) Create a second Telegram bot if you want to a dedicated bot to send admin messages (later referred to as admin_msg_bot)
- Go to the directory where the script is located
- Edit `credentials/telegram_bot.json.example`:
  - Add your user_msg_bot information in `user_msg_bot`
  - (optional) Add your admin_msg_bot information in `admin_msg_bot` and change the value of `admin_msg_bot.enabled` to `1`.
  - Add `chat_id` of your Telegram account or whoever is the admin
  - Add `chat_id`s of the users you want to receive notifications, including the admin if applicable
  - Save the file and remove the `.example` extension
- Ask all your users to search and start the chat channel with user_msg_bot
- (optional) Ask your admin to search and start the chat channel with admin_msg_bot
- Run `main.py`