import logging

# Logging settings
LOG_LEVEL = logging.DEBUG
CONSOLE_LOG_LEVEL = logging.DEBUG
FILE_LOG_LEVEL = logging.DEBUG
LOGGER_NAME = 'root'

# Etherscan settings
TXS_PER_RESPONSE = 10000

# Opensea settings
ID_DELTA = 30 # max gap between start and end ID

# Ethereum settings
NULL_ADDRESS = "0x0000000000000000000000000000000000000000"
AVERAGE_BLOCK_TIME = 15 # in seconds

# NFT Collection specific
START_ID = 0
END_ID = 10000
CONTRACT_ADDRESS = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"