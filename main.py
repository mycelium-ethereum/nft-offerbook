import gevent
from gevent import monkey
monkey.patch_all();

import settings
from utils import *

def get_opensea_offers() -> List[Dict]:
    jobs = []
    start_id = settings.START_ID
    ct = 0
    while start_id < 1000:
        ct += 1
        jobs.append(
            gevent.spawn(
                opensea.get_all_offers, 
                opensea.prepare_id_string(
                    start_id, 
                    start_id + settings.ID_DELTA
                )
            )
        )
        if ct == 3: 
            ct = 0
            print(start_id)
            print('sleeping now...')
            time.sleep(2)
        start_id += settings.ID_DELTA
    _ = gevent.joinall(jobs)
    return [job.value for job in jobs]

start_time = time.time()
offers = get_opensea_offers()
print(offers)
print(f"Time taken: {time.time() - start_time}")

# print(opensea.get_all_offers(opensea.prepare_id_string(0, 30)))