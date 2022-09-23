from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN=os.getenv('TOKEN')

intents = discord.Intents.default() 
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

# Bot is going crazy
@bot.event
async def on_message(message):
    await message.channel.send(f'{message.author},{bot.user}')
    await bot.process_commands(message)
bot.run(TOKEN)