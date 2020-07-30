# bot.py
import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event 
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    haikyu_quotes = [
        "Hey, Hey, Hey!", 
        "Don't mind! Don't mind!"
    ]
    help_text = (
        "I'm a huge fan of Haikyu!! So " 
        "I'll respond to certain text in your messages " 
        "every now and then if it relates. In particular"
        " I can't resist: " 
        "'quote', 'bokuto mode', 'volleyball', or you can "
        "@mention me."
    )


    if message.content.find('quote') > -1:
        # add a reaction
        
        # response message 
        response = random.choice(haikyu_quotes)
        await message.channel.send(response)
    elif message.content.find('sorry') > -1: 
        response = "Don't mind! Don't mind!"
        await message.channel.send(response)
    elif message.content.find("hey hey hey") > -1 or message.content.find("bokuto mode") > -1:
        response = "https://www.youtube.com/watch?v=HvXcTVSArX8"
        await message.channel.send(response)
    elif message.content == "help":
        response = help_text
        await message.channel.send(response)
    

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        f.write(f'Unhandled exception: {args[0]}\n')
        
client.run(TOKEN)