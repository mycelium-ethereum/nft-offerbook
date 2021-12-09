from utils import *
from fastapi import FastAPI

alert(f"{os.getenv('NAME')}: Starting server for Opensea")
app = FastAPI()
logger = setup_custom_logger('root')
setup_file_logger('opensea', logger)

@app.get(f"/floor")
async def root(slug: str):
    try:
        floor = opensea.get_floor(slug)
        return {'result': 1, 'data': {'price': floor}}
    except:
        alert(f"{os.getenv('NAME')}: Some bug for {slug}")
        return {'result': 0, 'data': {'error': 'Opensea API bug'}}