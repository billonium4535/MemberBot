import discord
import random

USER_ID = YOUR_USER_ID
active = True

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="South Park ｜ mb! help"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global active
    if (message.content.lower()).startswith('mb! help'):
        await message.channel.send('Member typing mb! member')

    elif message.content.lower() == "!memberStart":
        active = True
    elif message.content.lower() == "!memberStop":
        active = False

    elif 'member' in (message.content.lower()) and active:
        if message.author.id != USER_ID:
            quotes = open("quotes.txt").read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)

    elif 'remember' in (message.content.lower()) and active:
        if message.author.id != USER_ID:
            quotes = open("quotes.txt").read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)

client.run("YOUR-TOKEN-HERE")
