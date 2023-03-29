import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()#loads files from a .dotenv

# the 'main' function of the discord integration stuff. executes all the discord functionality
def startBot():
    
    # Gets token from .env file in the project
    TOKEN = os.getenv("DISCORD_TOKEN")
    description = '''This bot got memes'''# writes description for the bot

    # intents setup
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.guilds = True

    #sets up the commands
    bot = commands.Bot(command_prefix='?', description = description, intents = intents)

    #Events and Commands Below
    # ------------------------------------
    @bot.event 
    async def on_ready():
        '''Startup event, says that the bot is now running'''
        print(f"{bot.user} is now running!")
    
    @bot.command()
    async def ping(ctx):
        '''Checks the latency of the bot, creates it within an embed'''
        embedVar = discord.Embed(title="Pong", description="Pong", color=0x00ff00)
        embedVar.add_field(name="Latency", value=str(round(bot.latency * 1000)), inline=False)
        await ctx.send(embed=embedVar)

    @bot.command()
    async def test(ctx, arg):
        '''Test command, repeats what you said. Use Quotes for literals'''
        await ctx.send(arg)
    
    @bot.command()
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)
    
    @bot.command()
    async def joined(ctx, member: discord.Member):
        """Says when the member joined, and some more info"""
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
    #checks for bad arguments
    @joined.error
    async def joined_error(ctx, error):
        '''Relays bad argument error'''
        if isinstance(error, commands.BadArgument):
            await ctx.send("Please tag a member! [prefix]joined @(member)")
            
    
    bot.run(TOKEN)