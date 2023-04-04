import requests
import random
import os
from imgurpython import ImgurClient
from dotenv import load_dotenv

load_dotenv()
# sets up imgur client and grabs the ids from ENV
client_id = os.getenv("IMGUR_CLIENTID")
client_secret = os.getenv("IMGUR_CLIENT_SECRET")
access_token = os.getenv("IMGUR_ACCESS_TOKEN")
refresh_token = os.getenv("IMGUR_REFRESH_TOKEN")

#sets the client using the IDs
im_client = ImgurClient(client_id, client_secret, access_token, refresh_token)

def getMeme():
    '''Grabs a meme that is hosted on Imgur'''
    # grabs a gallery of memes and stores
    meme_list = im_client.memes_subgallery()
    randomMeme = random.choice(meme_list)
    return randomMeme.link

