import requests
import random
import os
from imgurpython import ImgurClient
from dotenv import load_dotenv

load_dotenv()
#sets up imgur client
#grabs the ids from ENV
client_id = os.getenv("IMGUR_CLIENTID")
client_secret = os.getenv("IMGUR_CLIENT_SECRET")
access_token = os.getenv("IMGUR_ACCESS_TOKEN")
refresh_token = os.getenv("IMGUR_REFRESH_TOKEN")
#sets the client using the IDs
im_client = ImgurClient(client_id, client_secret, access_token, refresh_token)

#authorization (not on rn)
#authorization_url = im_client.get_auth_url()

memes = im_client.memes_subgallery()
for item in memes:
    print(item.link)

def getMeme():
    
    
    memeURLs = ["https://i.imgur.com/cqVMHfX.jpg", "https://i.imgur.com/qDiMN4n.jpg", "https://i.imgur.com/xrIl15t.jpg"]

    meme_url = random.choice(memes)
    #print(meme_url)

    return requests.get(meme_url)

