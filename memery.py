import os

import discord

from memes import *

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

if __name__ == "__main__":

	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
	
		if message.content.startswith('!bf '):

			distracted_boyfriend(message)

			await message.channel.send(file=discord.File('output/boyfriend.jpg'))
		
		if message.content.startswith("!whatcat "):
			whatcat(message)

			await message.channel.send(file=discord.File('output/whatcat.jpg'))

		if message.content.startswith("!buttons "):
			two_buttons(message)

			await message.channel.send(file=discord.File('output/two_buttons.jpg'))

		if message.content.startswith("!meme help"):
			embed = give_help()

			await message.channel.send(embed=embed)

	client.run(TOKEN)
