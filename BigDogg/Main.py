import discord
from Responses import *
from WebInterface import *

client = discord.Client()
begin_command = "dogg"


def check_if_author_is_stonks(author):
    """
    Check if the message author is Stonks (me).
    :param author: The author to be checked with.
    :return: Boolean value stating if the author is stonks.
    """
    return author.name == "Stonks" and author.discriminator == "4423"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    if content.startswith(begin_command) or content.endswith(begin_command):
        # Add a new entry to the hello list.
        if ("add to hello list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(add_to_list("hello", hello_list, content, 5))

        # Remove an entry from the hello list.
        elif ("remove from hello list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(remove_from_list("hello", hello_list, content, 5))

        # Add a new entry to the hello candidate list.
        elif ("add to hello candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(add_to_list("hello candidate", hello_candidates, content, 6))

        # Remove an entry from the hello candidate list.
        elif ("remove from hello candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(remove_from_list("hello candidate", hello_candidates, content, 6))

        # Add a new entry to the bark list.
        elif ("add to bark list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(add_to_list("bark", bark_list, content, 5))

        # Remove an entry from the bark list.
        elif ("remove from bark list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(remove_from_list("bark", bark_list, content, 5))

        # Add a new entry to the bark candidate list.
        elif ("add to bark candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(add_to_list("bark candidate", bark_candidates, content, 6))

        # Remove an entry from the bark candidate list.
        elif ("remove from bark candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(remove_from_list("bark candidate", bark_candidates, content, 6))

        # Print the hello list.
        elif ("print hello list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(print_list("hello", hello_list))

        # Print the hello candidate list.
        elif ("print hello candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(print_list("hello candidate", hello_candidates))

        # Print the bark list.
        elif ("print bark list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(print_list("bark", bark_list))

        # Print the bark candidate list.
        elif ("print bark candidate list" in content) and check_if_author_is_stonks(message.author):
            await message.channel.send(print_list("bark candidate", bark_candidates))

        # Request help.
        elif "help" in content:
            await message.channel.send(send_help())

        # Print all the available commands.
        elif "all commands" in content:
            await message.channel.send(print_all_commands())

        # Execute a command (currently unavailable).
        elif "execute" in content:
            if len(message.attachments):
                await message.channel.send(execute_attachments(message.attachments))
            else:
                await message.channel.send(execute(content))

        # Search the candidates and say hello if requested.
        elif (x in content for x in hello_candidates):
            await message.channel.send(say_hello())

        # Add two values.
        elif "add" in content:
            await message.channel.send(perform_addition(content))

        # Subtract two values.
        elif "sub" in content:
            await message.channel.send(perform_subtraction(content))

        # Multiply two values.
        elif "mul" in content:
            await message.channel.send(perform_multiplication(content))

        # Divide two values.
        elif "div" in content:
            await message.channel.send(perform_division(content))

        # Bark.
        else:
            await message.channel.send(dogg_bark(content))

client.run(os.environ["DISCORD_BOT_TOKEN"])
