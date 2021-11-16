#This function gets text to speech from google and plays it in a voice chat
from gtts import gTTS
import discord

async def t2s(client, message):
  #get voice chat that your currently in
  voice_chat_ID = message.author.voice
  #now gather the mp3 data from google
  tts = gTTS(message.content[4:-1])
  tts.save('tts.mp3')
  #connect to the chat, play the clip
  vc = await voice_chat_ID.channel.connect()
  vc.play(discord.FFmpegPCMAudio('tts.mp3'))