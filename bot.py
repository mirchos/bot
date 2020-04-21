import discord
import telegramPart
from discord.ext import commands


TOKEN = 'NDU2MjA4MzI4OTg5NjA1OTEw.XpDk4A.X5Bg0CnClGYnRV4mRMKjg-wPHyk'
bot = commands.Bot(command_prefix='!')
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    print(message.content)
    if message.content != '':
        telegramPart.send_message(message.content)

client.run(TOKEN)
