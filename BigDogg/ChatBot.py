from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat_bot_dictionary = {}
chat_bot_trainers = {}
chat_bot_enables = {}
previous_bot_input = {}

private_chat_bots = {}
private_chat_bot_trainers = {}
private_chat_bot_previous_input = {}


def create_new_chat_bot():
    """
    Create a new chat bot.
    :return: The newly created chat bot.
    """
    return ChatBot(
        "BigDogg",
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.SpecificResponseAdapter',
            'chatterbot.logic.MathematicalEvaluation',
            'chatterbot.logic.SpecificResponseAdapter',
        ],
        database_uri='sqlite:///database.sqlite3'
    )


def create_new_chat_bot_trainer(chat_bot):
    """
    Create a new chat bot trainer.
    :param chat_bot: The chat bot to be used.
    :return: The new trainer.
    """

    return ListTrainer(chat_bot)


def train_chat_bot(server_name, response):
    """
    Train the chatterbot using a single response string.
    :param server_name: The name of the server.
    :param response: The response string.
    :return: None.
    """

    chat_bot_trainers[server_name].train([response])


def talk_to_chat_bot(server_name, input_text):
    """
    Talk to the chat bot.
    :param server_name: The name of the server.
    :param input_text: The input text to submit.
    :return: The chat bot's reply.
    """

    return chat_bot_dictionary[server_name].get_response(input_text)


def enable_chat_bot(server_name):
    """
    Enable the chat bot for a particular server.
    :param server_name: The name of the server.
    :return: None
    """

    chat_bot_enables[server_name] = True
    return f"Chat bot enabled for server: {server_name}"


def disable_chat_bot(server_name):
    """
    Disable the chat bot for a particular server.
    :param server_name: The name of the server.
    :return: None
    """

    chat_bot_enables[server_name] = False
    return f"Chat bot disabled for server: {server_name}"


def enable_private_chat_bot(user_name):
    """
    Enable chat bot for a private message.
    :param user_name: The name of the user.
    :return: None.
    """

    try:
        null_bot = private_chat_bots[user_name]
        null_trainer = private_chat_bot_trainers[user_name]

    except KeyError:
        private_chat_bots[user_name] = create_new_chat_bot()
        private_chat_bot_trainers[user_name] = create_new_chat_bot_trainer(private_chat_bots[user_name])


def disable_private_chat_bot(user_name):
    """
    Disable the private chat bot.
    :param user_name: Name of the user.
    :return: None.
    """

    private_chat_bots.pop(user_name)
    private_chat_bot_trainers.pop(user_name)


def private_chat_bot_get_response(user_name, user_data):
    """
    Get a response from the bot.
    :param user_name: The name of the user.
    :param user_data: The user inputs.
    :return: The bot's response.
    """

    return private_chat_bots[user_name].get_response(user_data)


def train_private_chat_bot(user_name, training_string):
    """
    Train a private chat bot.
    :param user_name: The name of the user.
    :param training_string: The string to be used to train.
    :return: None
    """

    private_chat_bot_trainers[user_name].train([training_string])
