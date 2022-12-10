import discord
import random

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="South Park ｜ mb! help"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if (message.content.lower()).startswith('mb! help'):
        await message.channel.send('Member typing mb! member')

    elif 'member' in (message.content.lower()):
        if message.author.id != 920400004504498188:
            quotes = open("quotes.txt").read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)

    elif 'remember' in (message.content.lower()):
        if message.author.id != 920400004504498188:
            quotes = open("quotes.txt").read().splitlines()
            quote = random.choice(quotes)
            await message.channel.send(quote)

    elif message.content.lower().startswith("fuck_daniel"):
        if message.author.id == 296371822381891586:
            for i in range(10):
                await message.channel.send("<@364476443578728459>")

client.run("OTIwNDAwMDA0NTA0NDk4MTg4.YbjzTQ.XFs_4owMHqcWBrymRIog1bJYW08")
