'''This module handles all code relating to image databases-specifically pixiv
It's main goal is to retrieve and push images'''
import os
from pathlib import Path
from pixivpy3 import *
from dotenv import load_dotenv

load_dotenv()
pixiv_refresh_token = os.getenv("PIXIV_REFRESH_TOKEN")

api = AppPixivAPI()
api.auth(refresh_token=pixiv_refresh_token)
# client.authenticate("FzfBuNw4oS2lzyAg_SknPIKNlFfaydcpK3H__W60bLw")

def getImage():
    workingDirectory = os.listdir(f"{os.getcwd()}\my_pixiv_images")
                                  
    if workingDirectory == []:
        print("No files found in the directory.")
    else:
        for file in workingDirectory:
            os.remove(f"{os.getcwd()}\my_pixiv_images\{file}")


    json_result = api.illust_recommended()
    for illust in json_result.illusts[:1]:
        api.download(illust.image_urls.large, path=f"{os.getcwd()}\my_pixiv_images")
    files = os.listdir(f"{os.getcwd()}\my_pixiv_images")
    return files[0]
