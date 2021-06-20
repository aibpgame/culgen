import discord
import asyncio
import random
import os

client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
 
@client.event
async def on_message(message):
    if message.content.startswith('!생성'):
        channel = message.channel
        num = random.randrange(1000, 9999)
        num1 = random.randrange(1000, 9999)
        num2 = random.randrange(1000, 9999)
        num3 = random.randrange(100000, 999999)
        num4 = "-"
        msg = ('{0} {1} {2} {3} {4} {5} {6}'.format(num, num4, num1, num4, num2, num4, num3))
        await channel.send(msg)
        return None
 
client.run(os.environ['token'])