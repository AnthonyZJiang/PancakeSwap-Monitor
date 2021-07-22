import requests
import logging


class Telegram:
    def __init__(self, bot_token: str, admin_id: str = None) -> None:
        self._logger = logging.getLogger(__name__)
        self._bot_token = bot_token
        self.admin_id = admin_id
        self._chat_ids = []
        self._send_message_request_url = f'https://api.telegram.org/bot{self._bot_token}/sendMessage'

    def add_chat_id(self, chat_id: str) -> None:
        self._chat_ids.append(chat_id)

    def add_chat_ids(self, chat_ids: list) -> None:
        for chat_id in chat_ids:
            self.add_chat_id(chat_id)

    def remove_chat_id(self, chat_id: str) -> None:
        if chat_id in self._chat_ids:
            self._chat_ids.remove(chat_id)

    def send_message(self, chat_id: str, message: str) -> None:
        response = requests.post(url=self._send_message_request_url, data={'chat_id': {chat_id}, 'text': message}).json()
        if response['ok']:
            chat = response["result"]["chat"]
            user_full_name = chat["first_name"] + '_' + chat["last_name"]
            user_name = chat["username"] if "username" in chat else 'private'
            self._logger.debug(f'Telegram chat_id={chat_id} user={user_full_name}@{user_name} was notified.')
        else:
            self._logger.error(f'Telegram chat id {chat_id} was not notified.')
            self._logger.error(f'Response: {response}')

    def send_message_to_all(self, message: str) -> None:
        for chat_id in self._chat_ids:
            self.send_message(chat_id, message)

    def send_greetings_to_all(self, message: str = None) -> None:
        if not message:
            message = 'Pancakeswap Monitor is up running and monitoring.'
        self.send_message_to_all(message)

    def send_failure_message_to_all(self, message: str = None) -> None:
        if not message:
            message = 'Opps, Pancakeswap Monitor stopped working!'
        self.send_failure_message_to_all(message)

    def send_message_to_admin(self, messaage: str) -> None:
        if self.admin_id:
            self.send_message(self.admin_id, messaage)

    @staticmethod
    def token_to_message(token: dict) -> str:
        return f"\nToken name: {token['name']}\nSymbol: {token['symbol']}\nPrice: {token['price']}\nPrice BNB: {token['price_BNB']}"
