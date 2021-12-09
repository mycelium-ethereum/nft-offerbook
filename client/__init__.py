from dotenv import load_dotenv
load_dotenv();

import os
from client.Webhook import webhook
from client.Opensea import Opensea

opensea = Opensea(os.environ.get("OPENSEA_KEY"))