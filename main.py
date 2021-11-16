#Main file for handling events, all events will be handled in seperate
#files to reduce clutter
#Developed by Jason Foster 12/24/2020

from keep_alive import keep_alive
from t2s import t2s
from nhentai import nhentai
from kill_voice import kill_voice
from jukebox import jukebox
from pixiv import pixiv
from opGG import opGG
from dice import dice
from weather import weather
from at_here import at_here
import discord
import os

client = discord.Client()


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('tts'):
    await t2s(client, message)

  if len(message.content) < 7 and message.content.isdigit():
    await nhentai(client, message)

  if message.content.lower().startswith('pixiv'):
    await pixiv(client, message)

  if message.content.lower() == 'stop':
    await kill_voice(client, message)

  if message.content.lower().startswith('op.gg'):
    await opGG(client, message)

  if message.content.lower().startswith('jukebox'):
    await jukebox(client, message)

  if message.content.lower().startswith('roll '):
    await dice(client, message)

  if message.content.lower().startswith('weather'):
    await weather(client, message)

  if message.mention_everyone:
    await at_here(client, message)

keep_alive()
client.run(os.getenv('TOKEN'))
