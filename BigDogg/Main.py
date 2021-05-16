import discord
from DecisionTree import *

client = discord.Client()
begin_command = "dogg"
decision_tree = DecisionTree(begin_command)
personal_message_mode = False


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
        if "print decision tree" in content:
            await message.channel.send(decision_tree.print_all_nodes())
        else:
            await message.channel.send(decision_tree.get_callback(content)(message))

    else:
        try:
            if chat_bot_enables[message.guild.name]:
                train_chat_bot(message.content)
                new_response = str(talk_to_chat_bot(message.content))
                train_chat_bot(new_response)
                previous_bot_input[message.guild.name] = new_response

                await message.channel.send(new_response)

            elif (len(message.attachments) == 0) and ("http" not in message.content):
                train_chat_bot(message.content)

        except KeyError:
            chat_bot_enables[message.guild.name] = False
            train_chat_bot(message.content)


client.run(os.environ["DISCORD_BOT_TOKEN"])
