'''This module handles all the discord integration side of the bot'''
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
import meme_inte as mi
import pixiv_inte as pix


load_dotenv()#loads files from a .dotenv

# the 'main' function of the discord integration stuff. executes all the discord functionality
def start_bot():
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
    bot = commands.Bot(command_prefix='?', description = description, intents = intents)
    #Events and Commands Below
    # ------------------------------------
    @bot.event
    async def on_ready():
        '''Startup event, says that the bot is now running'''
        print(f"{bot.user} is now running!")
        try:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as excep:
            print(excep)

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

    @bot.tree.command(name="add")
    @app_commands.describe(left = 'First Num', right = 'Second Number')
    async def add(interaction: discord.Interaction, left: int, right: int):
        """Adds two numbers together."""
        await interaction.response.send_message(left + right)

    @bot.tree.command(name="mcount")
    async def mcount(interaction: discord.Interaction):
        '''Retrieves the count of members'''
        await interaction.response.send_message(f"This server has {interaction.guild.member_count} total members!")

    @bot.tree.command(name="stfu")
    @app_commands.describe(member="The member you want to ping")
    async def stfu(interaction: discord.Interaction, member: discord.Member):
        '''tells someone to stfu'''
        await interaction.response.send_message(f"<@{member.id}> STFU :eggmike:")

    @bot.tree.command(name="joined")
    @app_commands.describe(member="The member you wanna ping")
    async def joined(interaction: discord.Interaction, member: discord.Member):
        """Says when the member joined, and some more info"""
        await interaction.response.send_message(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

    @bot.tree.command(name="meme")
    async def meme(interaction: discord.Interaction):
        '''Sends a meme from imgur'''
        response = mi.get_meme()
        await interaction.response.send_message(response)
    
    @bot.tree.command(name="pixiv")
    async def pixiv(interaction: discord.Interaction):
        '''Sends a random image from pixiv'''
        file = pix.getImage()

        with open(f"my_pixiv_images\{file}", 'rb') as f:
            image = discord.File(f)
        await interaction.response.send_message(file=image)

    bot.run(discord_token)
