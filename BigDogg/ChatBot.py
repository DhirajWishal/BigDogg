from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat_bot_enables = {}
previous_bot_input = {}

chat_bot = ChatBot(
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

chat_bot_trainer = ListTrainer(chat_bot)


def train_chat_bot(response):
    """
    Train the chatterbot using a single response string.
    :param response: The response string.
    :return: None.
    """
    chat_bot_trainer.train([response])


def talk_to_chat_bot(input_text):
    """
    Talk to the chat bot.
    :param input_text: The input text to submit.
    :return: The chat bot's reply.
    """
    return chat_bot.get_response(input_text)


def enable_chat_bot(server_name):
    """
    Enable the chat bot for a particular server.
    :param server_name: The name of the server.
    :return: Nonde
    """
    chat_bot_enables[server_name] = True


def disable_chat_bot(server_name):
    """
    Disable the chat bot for a particular server.
    :param server_name: The name of the server.
    :return: Nonde
    """
    chat_bot_enables[server_name] = False
