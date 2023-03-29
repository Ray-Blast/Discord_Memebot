import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()#loads files from a .dotenv

# the 'main' function of the discord integration stuff. executes all the discord functionality
def startDiscordInte():
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix='!', intents = intents)

    @client.event
    async def on_ready():
        print("we are logged in")