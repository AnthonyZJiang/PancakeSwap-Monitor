import json
import re
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class PancakeSwapAPI:
    __BASE_URL = "https://api.pancakeswap.info/api/v2/"
    """
    Basic API request wrapper for PancakeSwap
    Scott Burlovich (github.com/scottburlovich)
    Last Update: May 9, 2021
    """

    def __init__(self, base_url=__BASE_URL):
        self.base_url = base_url
        self.request_timeout = 60
        self.session = requests.session()
        retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def __get(self, request_url: str):
        """
        GET request wrapper
        :param request_url: str
        """
        response = self.session.get(request_url, timeout=self.request_timeout)
        response.raise_for_status()
        return json.loads(response.content.decode('utf-8'))

    def tokens(self, address: str = None):
        """
        If address parameter is specified, returns the token information, based on address.
        Otherwise, returns the tokens in the top ~1000 pairs on PancakeSwap, sorted by reserves.
        :type address: str
        :return: Dict
        """
        if address:
            address = address.replace(' ', '')
            if not re.match("^0x([A-Fa-f0-9]{40})$", address):
                raise ValueError(f"Provided address hash ({address}) is not in a valid format.")

        url = f"{self.base_url}tokens{'/' + address if address is not None else ''}"
        return self.__get(url)