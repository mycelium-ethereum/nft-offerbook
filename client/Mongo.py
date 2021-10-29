import os
import ssl
import logging
from typing import List, Dict
from pymongo import MongoClient
from datetime import datetime, timedelta

class Mongo:
    def __init__(self, url: str):
        self.logger = logging.getLogger('root')
        self.client = MongoClient(url, ssl=True, ssl_cert_reqs=ssl.CERT_NONE, readPreference='nearest')