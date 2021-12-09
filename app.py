from utils import *
from fastapi import FastAPI

app = FastAPI()
logger = setup_custom_logger('root')
setup_file_logger(os.getenv("OPENSEA_SLUG"), logger)

@app.get(f"/floor/{os.getenv('OPENSEA_SLUG')}")
async def root():
    try:
        floor = opensea.get_floor(os.getenv('OPENSEA_SLUG'))
        return {'result': 1, 'data': {'price': floor}}
    except:
        return {'result': 0, 'data': {'error': 'Opensea API bug'}}