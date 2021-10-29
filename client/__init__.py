from dotenv import load_dotenv
load_dotenv();

import os
import json
import settings
from web3 import Web3
from client.Mongo import Mongo
from client.Webhook import webhook
from client.Opensea import Opensea
from client.Etherscan import Etherscan

mongo = Mongo(os.environ.get("MONGO_URL"))
opensea = Opensea(os.environ.get("OPENSEA_KEY"))
etherscan = Etherscan(os.environ.get("ETHERSCAN_KEY"))
web3 = Web3(Web3.HTTPProvider(os.environ.get("ETH_HTTP_URL")))