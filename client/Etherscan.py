import json
import requests

class Etherscan:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_abi(self, contract_address):
        request_string = (
            "https://api.etherscan.io/api"
            "?module=contract"
            "&action=getabi"
            f"&address={contract_address}"
            f"&apikey={self.api_key}"
        )
        response = requests.get(request_string)
        result = response.json()['result']
        return json.loads(result)