from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('TOKEN')

intents = discord.Intents.default() # or .all() if you ticked all, that is easier
intents.members = True # If you ticked the SERVER MEMBERS INTENT

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="cast_types_1",help="cast_types responds changing the type of nro")
async def cast_types_1(ctx,nro):
    await ctx.send(f"{type(nro)},{nro}")

@bot.command(name="cast_types_2",help="cast_types responds changing the type of nro but starting the function")
async def cast_types_2(ctx,nro:int):
    await ctx.send(f"{type(nro)},{nro}")
bot.run(TOKEN)