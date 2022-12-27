import discord
from discord.ext import commands
import requests



if __name__ == '__main__':

    TOKEN = 'MTA1NjM2MjY5Mzg4OTYzNDMxNA.GzDUK4.0BLIN6BSx0biFcivSSz4zv-Mzdpc1nlGl79RdI'
    intents = discord.Intents.default()
    intents.members = True
    client = commands.Bot(command_prefix='!', intents = intents)

    

client.run(TOKEN)