from helpers import Telegram


class PCSCriticalError(Exception):
    def __init__(self, message: str = '', telegram:Telegram = None):
        super().__init__(message)
        if telegram:
            telegram.send_message_to_admin(message)