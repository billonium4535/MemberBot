import discord
import random
import os

USER_ID = 710613961875259527
active = True

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="South Park ｜ mb! help"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    local_current_directory = os.path.dirname(__file__)
    local_file_path = os.path.join(local_current_directory, "quotes.txt")
    global active
    if message.author.bot:
        return

    if message.content.lower() == "!memberstart" and not active:
        active = True
        await message.channel.send("Started membering")
    elif message.content.lower() == "!memberstop" and active:
        active = False
        await message.channel.send("Stopped membering")

    elif 'member' in (message.content.lower()) and active:
        if message.author.id != USER_ID:
            quotes = open(local_file_path).read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)

    elif 'remember' in (message.content.lower()) and active:
        if message.author.id != USER_ID:
            quotes = open(local_file_path).read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)


current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, "token.txt")
token = open(file_path)
client.run(token.read())
