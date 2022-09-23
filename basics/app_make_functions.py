from discord.ext import commands
import discord, os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('TOKEN')

intents = discord.Intents.default() 
intents.members = True 

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.command(name="foo",help="foo responds with bar")
async def foo(msg):
    await msg.send(f"BAAAAR")

@bot.command(name="bar",help="bar responds with foo")
async def bar(msg):
    await msg.send(f"FOO")

@bot.command(name="iloveyou",help="iloveyou responds with Love")
async def iloveyou(msg):
    await msg.send(f"i love you too")
bot.run(TOKEN)