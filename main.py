import json
import logging
import os

from helpers import initiate_logger, Telegram
from pancakeswap import PCSMonitor

VERSION = '1.2.1'

def main():
    initiate_logger()
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.info(f'PancakeSwap Monitor v{VERSION}')

    telegram_bot_info = json.load(open(os.path.join('credentials','telegram_bot.json'), 'r'))
    if 'admin_msg_bot' in telegram_bot_info and telegram_bot_info['admin_msg_bot']['enabled']:
        admin_bot = telegram_bot_info['admin_msg_bot']['token']
    else:
        admin_bot = None

    telegram = Telegram(telegram_bot_info['user_msg_bot']['token'], admin_bot, telegram_bot_info['admin_id'])
    telegram.add_chat_ids(telegram_bot_info['chat_ids'])
    telegram.send_greetings_to_users()

    while True:
        monitor = PCSMonitor(telegram)
        try:
            monitor.start_monitor()
        except KeyboardInterrupt:
            logging.info('Keyboard interrupt... Stopping...')
            telegram.send_message_to_users('PancakeSwap Monitor is taking a break. You will be informed when I get back up.')
            telegram.send_message_to_admin('PancakeSwap Monitor has been taken done by keyboard interruption.')
            break
        except:
            #TODO more known exception handling
            logging.exception('Unknown error', exc_info=True)
            telegram.send_message_to_admin('A critical error occurred. PancakeSwap Monitor is restarting.')
        
if __name__ == '__main__':
    main()