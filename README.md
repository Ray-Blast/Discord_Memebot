# Discord Meme Bot

This is a simple bot that interacts with the Discord API and Imgur API to provide high quality memes and utilities

# Installation

In order to use it, you must have a python venv enviroment, and a .env with the proper credentials (your own bot token, imgur credentials, etc etc)
Steps for windows:

```command prompt
python -m venv venv
.\venv\Scripts\activate.ps1
pip install -r requirements.txt
```
From there, make a file called ".env" and place it in the root folder, format it below

Your .env would look something like this:

```.env
DISCORD_TOKEN="YOUR_TOKEN_HERE"

IMGUR_CLIENTID="ID_HERE"
IMGUR_CLIENT_SECRET="SECRET_HERE"
IMGUR_ACCESS_TOKEN="TOKEN_HERE"
IMGUR_REFRESH_TOKEN="REFRESH_HERE"

IMGUR_ACCOUNT_ID="ID_HERE"
```

populate it with your tokens, then run program and done.


### Make sure to read license, but you are not allowed to resell bot or anything like that. This is moostly for educational and fun purposes. 
