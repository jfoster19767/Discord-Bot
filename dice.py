#scripts to handle coin flips and dice rolls
import random
import discord

async def dice(client, message):
	#First we should filter messages that start with roll but is unrelated to dice
	input_args = message.content.split(' ')
	
	output_string = ""
	total = 0

	for i in range(1, len(input_args)):
			roll_args = str.split(input_args[i], "d")
			if "+" in roll_args[1]:
					operator_args = str.split(roll_args[1], "+")

					output_string = output_string + " ("

					for j in range(0, int(roll_args[0])):
							roll = random.randint(1,int(operator_args[0]))
							total = total + roll
							output_string = output_string + str(roll) + " + "

					if len(operator_args) != 1:
							output_string = output_string + operator_args[1] + ") +"
							total = total + int(operator_args[1])
					else:
							output_string = output_string[0:-3] + ") +"
			elif "-" in roll_args[1]:
					operator_args = str.split(roll_args[1], "-")

					output_string = output_string + " ("

					for j in range(0, int(roll_args[0])):
							roll = random.randint(1,int(operator_args[0]))
							total = total + roll
							output_string = output_string + str(roll) + " + "

					if len(operator_args) != 1:
							output_string = output_string[0:-3] + " - " + operator_args[1] + ") +"
							total = total - int(operator_args[1])
					else:
							output_string = output_string[0:-3] + ") +"
			else:
					output_string = output_string + " ("

					for j in range(0, int(roll_args[0])):
							roll = random.randint(1,int(roll_args[1]))
							total = total + roll
							output_string = output_string + str(roll) + " + "
							
					output_string = output_string[0:-3] + ") +"
					
	output_string = output_string[1:-2]
	output_string = output_string + " = " + str(total)		
	await message.channel.send(output_string)
