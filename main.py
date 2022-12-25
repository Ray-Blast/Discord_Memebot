import discord
from discord.ext import commands
import requests



if __name__ == '__main__':

    TOKEN = 'MTA1NjM2MjY5Mzg4OTYzNDMxNA.GfIWi9.i5jPQo8PE9XHIbMWlli65mXO9y99EH8rT27RGc'
    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix='!', intents = intents)

    
