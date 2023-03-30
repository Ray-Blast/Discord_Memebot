import requests




def getMeme():
    meme_url = "https://twitter.com/i/status/1641422683924512769"

    return requests.get(meme_url)

