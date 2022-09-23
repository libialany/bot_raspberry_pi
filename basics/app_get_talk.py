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

@bot.event
async def on_message(message):
    # Not going crazy
    if message.author == bot.user: 
        return
    
    if message.content == 'hola':
        await message.channel.send(f'Holaaa 😃 {message.author}')
    if message.content == 'adios':
        await message.channel.send(f'Adios 🥺 {message.author}')

    await bot.process_commands(message)

bot.run(TOKEN)