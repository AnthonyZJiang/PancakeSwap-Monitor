import json
import logging
import os

from helpers import initiate_logger, Telegram
from pancakeswap import PCSMonitor

VERSION = '1.0.0'

initiate_logger()
logging.info(f'PancakeSwap Monitor v{VERSION}')

prev_server_time = 0
telegram_bot_info = json.load(open(os.path.join('credentials','telegram_bot.json'), 'r'))
telegram = Telegram(telegram_bot_info['token'], telegram_bot_info['admin_id'])
telegram.add_chat_ids(telegram_bot_info['chat_ids'])
telegram.send_greetings_to_all()

while True:
    monitor = PCSMonitor(telegram)
    try:
        monitor.start_monitor()
    except KeyboardInterrupt:
        logging.info('Keyboard interrupt... Stopping...')
        telegram.send_message_to_all('PancakeSwap Monitor is taking a break. You will be informed when I get back up.')
        break
    except:
        #TODO more known exception handling
        logging.exception('Unknown error', exc_info=True)
        telegram.send_message_to_admin('A critical error occurred. PancakeSwap Monitor is restarting.')
    