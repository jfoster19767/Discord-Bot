#handle @everyone and @here

import os
import random
import discord

async def at_here(client, message):
	file_list = os.listdir('Everyone')
	await message.channel.send(file=discord.File('Everyone/' + random.choice(file_list)))