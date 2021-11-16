#Script that handles requests to op.gg
async def opGG(client, message):
  #figure out how many people I'm looking up
  args = message.content.split(' ')
  if len(args) == 2:
    #only look up one person
    await message.channel.send("https://na.op.gg/summoner/userName=" + args[1])
  elif len(args) <= 6:
    #you should realisticly not need to look up more than 5 people
    #remove 'op.gg'
    args = args[1:]
    #sort through the remaining summoners and have them in a string
    summoner_list = ''
    for summoner in args:
      summoner_list = summoner_list + summoner
    await message.channel.send('https://na.op.gg/multi/query=' + summoner_list)
  else:
    await message.channel.send("I'm sorry, but I don't know how to do that")