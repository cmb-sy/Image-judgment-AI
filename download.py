import sys
import os
import time
from urllib.request import urlretrieve
from tqdm import tqdm
from flickrapi import FlickrAPI

key = "0939fdb36152a500c922ed2babb2dff2"
secret = "67d9e1be9ea55fa1"
wait_time = 1 # リクエストのパンクを防止のため

# 保存フォルダの指定
animalName = sys.argv[1]
saveDir = "image/" + animalName

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = animalName,
    per_page = 500,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence' # 返り値を一部指定
)

photos = result['photos']
# pprint(photos)

for i, photo in enumerate(tqdm(photos['photo'])):
    url_q = photo['url_q']
    filePath = saveDir + "/" + photo['id'] + ".jpg"
    if os.path.exists(filePath) : continue # 重複があればスキップ
    urlretrieve(url_q, filePath)
    time.sleep(wait_time)