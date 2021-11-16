#Script to handle pixiv requests
async def pixiv(client, message):
  if message.content[6:].isdigit():
    #only post weebshit in weeb shit
    weeb_ID = client.get_channel(575148028621488140)
    #0 does not exist
    if message.content != '0':
      await weeb_ID.send('https://www.pixiv.net/en/artworks/' + message.content[6:])