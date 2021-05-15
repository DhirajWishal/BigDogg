import discord
from Responses import *

client = discord.Client()
begin_command = "dogg"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(begin_command) or message.content.endswith(begin_command):
        content = message.content.lower()

        if "help" in content:
            await message.channel.send(send_help())

        elif ("hello" in content) or ("hey" in content) or ("heyy" in content):
            await message.channel.send(say_hello())

        elif "add" in content:
            await message.channel.send(perform_addition(content))

        elif "sub" in content:
            await message.channel.send(perform_subtraction(content))

        elif "mul" in content:
            await message.channel.send(perform_multiplication(content))

        elif "div" in content:
            await message.channel.send(perform_division(content))

        elif "execute" in content:
            await message.channel.send(execute(content))

        else:
            await message.channel.send(dogg_bark(content))

client.run('ODQyOTk4MDQxNzE0NjIyNDY0.YJ9dGw.s8i71h8mGJMZLEwXWBxcPuaYzeI')
