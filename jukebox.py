#script to handle youtube.dl
from __future__ import unicode_literals
import youtube_dl
import discord
import os

async def jukebox(client, message):
  if os.path.exists('Tunes.mp3'):
    os.remove('Tunes.mp3')
  args = message.content.split(' ')
  ydl_opts = {
      'outtmpl': 'Tunes.mp3',
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
  }
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([args[1]])
      voice_chat_ID = message.author.voice
      vc = await voice_chat_ID.channel.connect()
      vc.play(discord.FFmpegPCMAudio('Tunes.mp3'))