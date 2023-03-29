import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()#loads files from a .dotenv

# the 'main' function of the discord integration stuff. executes all the discord functionality
def startBot():
    
    TOKEN = os.getenv("DISCORD_TOKEN")
    description = '''This bot got memes'''

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    intents.guilds = True

    bot = commands.Bot(command_prefix='?', description = description, intents = intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running!")
    
    @bot.command()
    async def ping(ctx):
        embedVar = discord.Embed(title="Pong", description="Pong", color=0x00ff00)
        embedVar.add_field(name="Latency", value=str(round(bot.latency * 1000)), inline=False)
        await ctx.send(embed=embedVar)

    @bot.command
    async def test(ctx, arg):
        await ctx.send(arg)

    @bot.command()
    async def joined(ctx, member: discord.Member):
        """Says when a member joined."""
        await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')
    
    bot.run(TOKEN)