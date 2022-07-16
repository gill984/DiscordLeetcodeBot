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

token_file = open("pw.txt", "r")
token = token_file.read()
token_file.close()
client.run(token)