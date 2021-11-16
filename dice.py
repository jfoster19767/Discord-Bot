#scripts to handle coin flips and dice rolls
import random
import discord

async def dice(client, message):
	#First we should filter messages that start with roll but is unrelated to dice
	message_list = message.content.split(' ')
	if len(message_list) == 2:
		#Now I need to figure out how many dice I'm rolling
		if message_list[1][0].isdigit():
		#rolling multiple dice
			roll_string = message_list[1].split('d')
			number_of_dice = roll_string[0]
			number_of_dice = int(number_of_dice)
			type_of_dice = roll_string[1]
			type_of_dice = int(type_of_dice)
			# now roll that die and add the result
			result_list = [None] * number_of_dice
			for x in range(number_of_dice):
				result_list[x - 1] = random.randint(1, type_of_dice)
			await message.channel.send(str(result_list) + " = " + str(sum(result_list)))
				
		else:
			if message.content.lower() == 'roll d2':
				#throw a coin
				result = random.randint(1,2)
				await message.channel.send(file=discord.File('Dice_bag/d2_' + str(result) + '.png'))

			elif message.content.lower() == 'roll d4':
				result = random.randint(1,4)
				await message.channel.send(file=discord.File('Dice_bag/d4_' + str(result) + '.png'))

			elif message.content.lower() == 'roll d6':
				result = random.randint(1,6)
				await message.channel.send(file=discord.File('Dice_bag/d6_' + str(result) + '.png'))

			elif message.content.lower() == 'roll d8':
				result = random.randint(1,8)
				await message.channel.send(file=discord.File('Dice_bag/d8_' + str(result) + '.png'))
			#generic catch all for any other dice
			else:
				result = random.randint(1, int(message.content[-1]))
				await message.channel.send(str(result))

	else:
		return