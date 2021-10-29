from __future__ import annotations
import sys
import time
import logging
import settings
from threading import Thread
from dataclasses import dataclass
from typing import List, Callable, Dict
from datetime import datetime, timedelta
from web3._utils.filters import LogFilter
from client import web3, webhook, mongo, opensea, etherscan

class Streaming:
    def __init__(self):
        self.logger = logging.getLogger(settings.LOGGER_NAME)
        self.errored = False

    def log_loop(self, event_filter: LogFilter, event_handler: Callable, poll_interval: float = 1):
        while True:
            try:
                for event in event_filter.get_new_entries():
                    event_handler(event)
            except Exception as e:
                self.logger.error(e)
                self.errored = True
                self.error = e
            time.sleep(poll_interval)

    def start_streaming(self, event: str, event_handler: Callable, **kwargs):
        self.logger.info(f"Opened stream for {event}")
        event_filter = self.contract.events[event].createFilter(fromBlock='latest', argument_filters=kwargs)
        thread = Thread(target=self.log_loop, args=[event_filter, event_handler], daemon=True)
        thread.start()

class Address:
    def __init__(self, address: str, name: str = None) -> None:
        self.name = name
        self.raw = address
        self.address = self.__parse()

    def __parse(self) -> str:
        if web3.isChecksumAddress(self.raw): return self.raw
        else: return web3.toChecksumAddress(self.raw)

class Contract(Streaming):
    def __init__(self, contract_address: str):
        super().__init__()
        self.contract = web3.eth.contract(
            address=contract_address,
            abi=etherscan.get_abi(contract_address)
        )