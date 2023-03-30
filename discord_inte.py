'''This module handles all the discord integration side of the bot'''
import os
import discord
import requests
import meme_inte as mi
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

load_dotenv()#loads files from a .dotenv

# the 'main' function of the discord integration stuff. executes all the discord functionality
def startBot():
    '''Function that begins the bot startup'''
    # Gets token from .env file in the project
    discord_token = os.getenv("DISCORD_TOKEN")
    description = '''This bot got memes'''# writes description for the bot

    # intents setup
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.guilds = True

    #sets up the commands
    bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), description = description, intents = intents)

    #Events and Commands Below
    # ------------------------------------
    @bot.event 
    async def on_ready():
        '''Startup event, says that the bot is now running'''
        print(f"{bot.user} is now running!")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
    
    @bot.tree.command(name="hello")
    async def hello(interaction: discord.Interaction):
        '''Slash command for saying hi!'''
        await interaction.response.send_message(f"Hi {interaction.user.mention}!", ephemeral=True)

    @bot.tree.command(name="repeat")
    @app_commands.describe(phrase = "What you want me to repeat?")
    async def repeat(interaction: discord.Interaction, phrase: str):
        '''Slash Command for repeating a phrase'''
        await interaction.response.send_message(f"{interaction.user.name} said: '{phrase}'")

    @bot.command(name="ping")
    async def ping(ctx):
        '''Checks the latency of the bot, creates it within an embed'''
        embed_var = discord.Embed(title="Pong", description="Pong", color=0x00ff00)
        embed_var.add_field(name="Latency", value=str(round(bot.latency * 1000)), inline=False)
        await ctx.send(embed=embed_var)

    @bot.command(name="test")
    async def test(ctx, arg):
        '''Test command, repeats what you said. Use Quotes for literals'''
        await ctx.send(arg)
    
    @bot.command(name="add")
    async def add(ctx, left: int, right: int):
        """Adds two numbers together."""
        await ctx.send(left + right)

    @add.error
    async def add_error(ctx, error):
        '''Relays bad argument error'''
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please give me two numbers! [prefix]add (num1) (num2)")
    
    @bot.command(name="mcount")
    async def mcount(ctx):
        '''Retrieves the count of members'''
        await ctx.send(f"This server has {ctx.guild.member_count} total members!")

    @bot.command(name="stfu")
    async def stfu(ctx, member: discord.Member):
        '''tells someone to stfu'''
        await ctx.send(f"<@{member.id}> STFU :eggmike:")
    
    @stfu.error
    async def stfu_error(ctx, error):
        '''Relays bad argument error'''
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please tag a member! [prefix]joined @(member)")

    @bot.command()
    async def joined(ctx, member: discord.Member):
        """Says when the member joined, and some more info"""
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
    #checks for bad arguments
    @joined.error
    async def joined_error(ctx, error):
        '''Relays bad argument error'''
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please tag a member! [prefix]joined @(member)")
      
    # Command that gets a meme and posts it
    @bot.command(name="meme")
    async def meme(ctx):
        response = mi.getMeme()
        if response.status_code == 200:
            with open('meme.jpg', 'wb') as f:
                f.write(response.content)
            with open('meme.jpg', 'rb') as f:
                await ctx.channel.send(file=discord.File(f, 'meme.jpg'))
        else:
            await ctx.channel.send('Failed to fetch meme :(')
    bot.run(discord_token)
