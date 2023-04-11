'''This module handles all code relating to image databases-specifically pixiv
It's main goal is to retrieve and push images'''
import os
from pixivpy3 import *
from dotenv import load_dotenv


load_dotenv()
pixiv_refresh_token = os.getenv("PIXIV_REFRESH_TOKEN")

api = AppPixivAPI()
api.auth(refresh_token=pixiv_refresh_token)
# client.authenticate("FzfBuNw4oS2lzyAg_SknPIKNlFfaydcpK3H__W60bLw")

def getImage():
    json_result = api.illust_detail(59580629)
    illust = json_result.illust
    print(">>> origin url: %s" % illust.image_urls['large'])