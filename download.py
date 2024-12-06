import os, time, sys

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint

# APIキーの情報
key = "0939fdb36152a500c922ed2babb2dff2"
secret = "67d9e1be9ea55fa1"
wait_time = 1 # リクエストのパンクを防止のため

# 保存フォルダの指定
animalName = sys.argv[1]
saveDir = "image/" + animalName

flickr = FlickrAPI(key, secret, format="parsed-json")
result = flickr.photos.search(
    text = animalName,
    per_page = 400,
    media = 'photos',
    sort = 'relevance',
    safe_search = 1,
    extras = 'url_q, licence' # 返り値を一部指定
)

photos = result['photos']
pprint(photos)