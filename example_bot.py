# This example requires the 'message_content' intent.

import discord
print(discord.__version__)

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTk3ODczNzc1ODkyNzcwODQ2.G6z8cW.wHc-42ipw0RZoDDnvdNh9lynEoLLV2SoYJM6ww')