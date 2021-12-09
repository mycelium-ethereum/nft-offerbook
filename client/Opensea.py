import settings
import requests
import logging
from typing import List, Dict

class Opensea:
    BASE_URL = "https://api.opensea.io/wyvern/v1"
    OFFSET = 50

    def __init__(self, api_key: str = None):
        self.api_key = api_key
        self.logger = logging.getLogger('root')
        if self.api_key is not None:
            self.headers = {
                "Accept": "application/json",
                "X-API-KEY": self.api_key,
            }
        else:
            self.headers = {"Accept": "application/json"}

    def get_floor(self, slug: str) -> int:
        try:
            response = requests.get(f"https://api.opensea.io/api/v1/collection/{slug}")
            return int(response.json()['collection']['stats']['floor_price'] * 1e18)
        except Exception as e:
            self.logger.error(e)
            raise Exception