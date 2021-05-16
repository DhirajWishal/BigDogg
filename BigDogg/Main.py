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


def handle_private_message(message):
    """
    Handle private messages (DMs).
    :param message: The user sent message.
    :return: The statement to be sent to the user.
    """
    user_name = message.author.name + "#" + message.author.discriminator

    enable_private_chat_bot(user_name)
    train_private_chat_bot(user_name, message.content)
    bot_response = str(private_chat_bot_get_response(user_name, message.content))
    train_private_chat_bot(user_name, bot_response)

    return bot_response


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    if message.channel.type == discord.ChannelType.private:
        await message.channel.send(handle_private_message(message))

    elif content.startswith(begin_command) or content.endswith(begin_command):
        if "print decision tree" in content:
            await message.channel.send(decision_tree.print_all_nodes())
        else:
            await message.channel.send(decision_tree.get_callback(content)(message))

    else:
        server_name = message.guild.name

        try:
            if chat_bot_enables[server_name]:
                train_chat_bot(server_name, message.content)
                new_response = str(talk_to_chat_bot(server_name, message.content))
                train_chat_bot(server_name, new_response)
                previous_bot_input[server_name] = new_response

                await message.channel.send(new_response)

            elif (len(message.attachments) == 0) and ("http" not in message.content):
                train_chat_bot(server_name, message.content)

        except KeyError:
            chat_bot_enables[server_name] = False
            chat_bot_dictionary[server_name] = create_new_chat_bot()
            chat_bot_trainers[server_name] = create_new_chat_bot_trainer(chat_bot_dictionary[server_name])
            train_chat_bot(server_name, message.content)


client.run(os.environ["DISCORD_BOT_TOKEN"])
