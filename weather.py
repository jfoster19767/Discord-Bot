#script to handle everything that works with openweathermap
import requests, json
import os

async def weather(client, message):
  #for now lets keep thing simple and pull current weather data for a city
  #Lets build the URL 
  base_url = "http://api.openweathermap.org/data/2.5/weather?"
  city = message.content.split(' ')
  complete_url = base_url + "appid=" + os.getenv('API_KEY') + "&q=" + city[1]
  #now pull data from the weather api
  response = requests.get(complete_url)
  x = response.json() 
  #We did get a response, R-right?
  if x["cod"] == "404":
    await message.channel.send("I'm sorry, I don't understand what to do")
  else:
    sky = x["weather"]
    sky = sky[0]
    air = x["main"]
    degrees = float(air['temp'])
    degrees = (degrees - 273.15) * 9/5 + 32
    await message.channel.send('http://openweathermap.org/img/wn/' + sky['icon'] + '@2x.png')
    await message.channel.send('The weather in ' + city[1] + ' is ' + sky['main'] + ' and it is currently ' + str(degrees) + ' degrees.')
