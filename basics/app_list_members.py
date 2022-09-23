from discord.ext import commands
import os
import discord
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(intents=intents, command_prefix=">")

listMembers = []

@client.event
async def on_ready():
    global listMembers
    for guild in client.guilds:
        for member in guild.members:
            listMembers.append(member.name)
@client.command(name="list_all_members",help="list_all_members")
async def lst_members(ctx):
    global listMembers
    result=""
    for i in listMembers:
        result += i+", "
    result=result[:-2]
    await ctx.send(f"The are joined to this server :{result}")
client.run(TOKEN)