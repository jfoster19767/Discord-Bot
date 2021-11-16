# this script will kick the discord bot from the voice chat incase
# I need to make it shut up
async def kill_voice(client, message):
  #find what voice channel I'm in from the list of all possible voice channels
  for voice_channel in client.voice_clients:
    await voice_channel.disconnect()
    #WARNING In theory this code kills ALL instances where the bot could be connected
    #But thats fine for now since it should only connect to one chat.