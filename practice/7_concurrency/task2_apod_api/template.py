import requests
from multiprocessing import Pool
import shutil
import os
import threading
import time

API_KEY = "hl9v3UacNJyy9IwWjlaiehDRS7Po0Z2zLwXexkBk"
APOD_ENDPOINT = 'https://api.nasa.gov/planetary/apod'
OUTPUT_IMAGES = './output'

def get_apod_metadata(metadata: dict) -> list:
    return requests.get(APOD_ENDPOINT,params=metadata).json()


def download_apod_images(metadata):

    if metadata['media_type'] == 'image':
        file = open(f"output/{metadata['date']}.jpg", "wb")
        response = requests.get(metadata['url'])
        file.write(response.content)
        file.close()
    else:
        pass
def main():
    metadata = get_apod_metadata({'start_date':'2021-08-01','end_date':'2021-09-30','api_key':API_KEY})
    #download_apod_images(metadata)
    starttime = time.time()
    pool = Pool()
    pool.map(download_apod_images, metadata)
    pool.close()
    endtime = time.time()
    print(f"Time taken {endtime - starttime} seconds")



if __name__ == '__main__':
    shutil.rmtree(OUTPUT_IMAGES)
    if not os.path.exists(OUTPUT_IMAGES):
        os.makedirs(OUTPUT_IMAGES)

    main()
