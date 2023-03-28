import discord
import os
from discord.ext import commands

def startDiscordInte():
    TOKEN = os.getenv("DISCORD_TOKEN")
    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix='!', intents = intents)