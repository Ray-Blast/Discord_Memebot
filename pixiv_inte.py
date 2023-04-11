'''This module handles all code relating to image databases-specifically pixiv
It's main goal is to retrieve and push images'''
import os
import random
import deepl
from pixivpy3 import *
from dotenv import load_dotenv

load_dotenv()
pixiv_refresh_token = os.getenv("PIXIV_REFRESH_TOKEN")
deepl_key = os.getenv("DEEPL_Key")
translator = deepl.Translator(deepl_key)

api = AppPixivAPI()
api.auth(refresh_token=pixiv_refresh_token)

def getFile(tag:str, search_type: str):
    '''Function that downloads and returns the path of an image form pixiv'''
    workingDirectory = os.listdir(f"{os.getcwd()}\my_pixiv_images")
                                  
    if workingDirectory == []:
        print("No files found in the directory.")
    else:
        for file in workingDirectory:
            os.remove(f"{os.getcwd()}\my_pixiv_images\{file}")

    match search_type:
        case "recommend":
            json_result = searchRecommended()
        case "tag":
            json_result = searchForFile(tag)
        case "related":
            json_result = search_related(tag)
            
    randomImg = random.randint(0, len(json_result)-1)
    illust = json_result.illusts[randomImg]
    print(len(json_result))

    api.download(illust.image_urls.large, path=f"{os.getcwd()}\my_pixiv_images")
    files = os.listdir(f"{os.getcwd()}\my_pixiv_images")
    return files[0]


def searchForFile(imgTag: str):
    jp_tag = translator.translate_text(text=imgTag, target_lang="JA")
    print(jp_tag)
    json_result = api.search_illust(word=jp_tag,search_target='partial_match_for_tags')
    return json_result

def searchRecommended():
    results = api.illust_recommended()
    return results

def search_related(tag):
    results = api.illust_related(tag)
    return results