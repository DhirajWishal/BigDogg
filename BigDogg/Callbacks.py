from Responses import *
from ChatBot import *
from WebInterface import *


def wrong_command_callback(message):
    """
    The wrong command function callback.
    :param message: The message structure from Discord.py.
    :return: The return from the wrong_command function.
    """
    return wrong_command()


def add_to_hello_list_callback(message):
    """
    Add to hello list callback.
    :param message: The message.
    :return: The return from the function.
    """
    return add_to_list("hello", hello_list, message.content.lower(), 5)


def add_to_hello_candidate_list_callback(message):
    """
    Add to hello candidate list callback.
    :param message: The message.
    :return: The return from the function.
    """
    return add_to_list("hello candidate", hello_candidates, message.content.lower(), 6)


def add_to_bark_list_callback(message):
    """
    Add to bark list callback.
    :param message: The message.
    :return: The return from the function.
    """
    return add_to_list("bark", bark_list, message.content.lower(), 5)


def add_to_bark_candidate_list_callback(message):
    """
    Add to bark candidate list callback.
    :param message: The message.
    :return: The return from the function.
    """
    return add_to_list("bark candidate", bark_candidates, message.content.lower(), 6)


def remove_from_hello_list_callback(message):
    """
    Remove an element from hello list.
    :param message: The message.
    :return: The return from the function.
    """
    return remove_from_list("hello", hello_list, message.content.lower(), 5)


def remove_from_hello_candidate_list_callback(message):
    """
    Remove an element from hello candidate list.
    :param message: The message.
    :return: The return from the function.
    """
    return remove_from_list("hello candidate", hello_candidates, message.content.lower(), 6)


def remove_from_bark_list_callback(message):
    """
    Remove an element from bark list.
    :param message: The message.
    :return: The return from the function.
    """
    return remove_from_list("bark", bark_list, message.content.lower(), 5)


def remove_from_bark_candidate_list_callback(message):
    """
    Remove an element from bark candidate list.
    :param message: The message.
    :return: The return from the function.
    """
    return remove_from_list("bark candidate", bark_candidates, message.content.lower(), 6)


def print_hello_list_callback(message):
    """
    Print the hello list.
    :param message: The message.
    :return: The return from the function.
    """
    return print_list("hello list", hello_list)


def print_hello_candidate_list_callback(message):
    """
    Print the hello candidate list.
    :param message: The message.
    :return: The return from the function.
    """
    return print_list("hello candidate list", hello_candidates)


def print_bark_list_callback(message):
    """
    Print the bark list.
    :param message: The message.
    :return: The return from the function.
    """
    return print_list("bark list", hello_list)


def print_bark_candidate_list_callback(message):
    """
    Print the bark candidate list.
    :param message: The message.
    :return: The return from the function.
    """
    return print_list("bark candidate list", bark_candidates)


def enable_chat_bot_callback(message):
    """
    Enable chat bot callback.
    :param message: The message.
    :return: The return from the function.
    """
    return enable_chat_bot(message.guild.name)


def disable_chat_bot_callback(message):
    """
    Disable chat bot callback.
    :param message: The message.
    :return: The return from the function.
    """
    return disable_chat_bot(message.guild.name)


def execute_attachments_callback(message):
    """
    Execute attachments callback.
    :param message: The message.
    :return: The function return.
    """
    return execute_attachments(message.attachments)


def execute_block_callback(message):
    """
    Execute block callback.
    :param message: The message.
    :return: The function return.
    """
    return execute(message.content)


def say_hello_callback(message):
    """
    Say hello callback.
    :param message: The message.
    :return: The function return.
    """
    return say_hello()


def send_help_callback(message):
    """
    Send help callback.
    :param message: The message.
    :return: The function return.
    """
    return send_help()


def print_all_commands_callback(message):
    """
    Print all commands callback.
    :param message: The message.
    :return: The function return.
    """
    return print_all_commands()


def perform_addition_callback(message):
    """
    Perform addition callback.
    :param message: The message.
    :return: The function return.
    """
    return perform_addition(message.content.lower())


def perform_subtraction_callback(message):
    """
    Perform subtraction callback.
    :param message: The message.
    :return: The function return.
    """
    return perform_subtraction(message.content.lower())


def perform_multiplication_callback(message):
    """
    Perform multiplication callback.
    :param message: The message.
    :return: The function return.
    """
    return perform_multiplication(message.content.lower())


def perform_division_callback(message):
    """
    Perform division callback.
    :param message: The message.
    :return: The function return.
    """
    return perform_division(message.content.lower())
