# bot that bring Sauce from nhentai.net
async def nhentai(client, message):
  #only post nsfw in nsfw
  nsfw_ID = client.get_channel(575147885406978048)
  #0 does not exist
  if message.content != '0':
    await nsfw_ID.send('https://nhentai.net/g/' + message.content)