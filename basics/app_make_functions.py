from discord.ext import commands
import discord, os, requests, random, string
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

@bot.command(name="cat",help="quiero gatos")
async def cat(msg):
    request_url = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(request_url).json()
    await msg.send(f" "+r[0]["url"])

@bot.command(name="iloveyou",help="iloveyou responds with Love")
async def iloveyou(msg):
    await msg.send(f"i love you too")

@bot.command(name="generate_passwd",help="Random String Generator")
async def generate_passwd(msg):
    await msg.send(f"".join(random.choice(string.ascii_letters + string.punctuation) for x in range(20)))


@bot.command(name="embed",help=".")
async def embed(ctx):
    embed=discord.Embed(title=ctx.author.display_name, url="https://realdrewdata.medium.com/", description="".join(random.choice(string.ascii_letters + string.punctuation) for x in range(20)), color=0xFF5733)
    request_url = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(request_url).json()
    embed.set_thumbnail(url=r[0]["url"])
    await ctx.send(embed=embed)

bot.run(TOKEN)
