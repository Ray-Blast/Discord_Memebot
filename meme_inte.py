import requests
import random

#placeholder


def getMeme():
    
    memeURLs = ["https://i.imgur.com/cqVMHfX.jpg", "https://i.imgur.com/qDiMN4n.jpg", "https://i.imgur.com/xrIl15t.jpg"]

    meme_url = random.choice(memeURLs)
    #print(meme_url)

    return requests.get(meme_url)

