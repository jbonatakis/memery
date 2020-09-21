import os
import random

import discord

from memes import *

TOKEN = os.environ['DISCORD_TOKEN']

client = discord.Client()

if __name__ == "__main__":

    no_no_words = ["phalanx", "paladin"]

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        elif message.content.startswith('!bf '):

            distracted_boyfriend(message)

            await message.channel.send(file=discord.File('output/boyfriend.jpg'))
        
        elif message.content.startswith("!whatcat "):
            whatcat(message)

            await message.channel.send(file=discord.File('output/whatcat.jpg'))

        elif message.content.startswith("!buttons "):
            two_buttons(message)

            await message.channel.send(file=discord.File('output/two_buttons.jpg'))

        elif message.content.startswith('!handshake '):
            handshake(message)

            await message.channel.send(file=discord.File('output/handshake.jpg'))

        elif message.content.startswith("!meme help"):
            embed = give_help()

            await message.channel.send(embed=embed)

        # elif "phalanx" in message.content.lower() or "paladin" in message.content.lower():
        elif any(word in message.content.lower() for word in no_no_words):
            chance = 1

            if random.randint(1, chance) == chance:
                await message.channel.send("<a:worryalarm:751369015519215626>"*7 + "\n<a:worryalarm:751369015519215626> **P WORD ALERT**<a:worryalarm:751369015519215626>\n" + "<a:worryalarm:751369015519215626>"*7)
            else:
                return

    client.run(TOKEN)
