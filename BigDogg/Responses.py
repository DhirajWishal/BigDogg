import random
import operator
import py_compile

hello_list = [
    "Whats good ma g!",
    "Go fu*k off!",
    "Hmm",
    "Get lost noob!",
    "Hello there!",
    "Whats up?",
    "What up?",
    "Dude im busy..",
    "LEAVE ME ALONE!",
    "Wrong command fool!"
]

bark_candidates = [
    "fuck you", "get lost", "suck my dick",
    "your trash", "your mom", "thats what she said",
    "ok boomer", "suck my dick", "fucking nigger"
]

bark_list = [
    "Yeah your mom loves me for the way i fuck you in your ass",
    "Suck my dick pussy",
    "Go say that to joe",
    "My dick is longer than your life fool",
    "Go suck your mom dumb ass",
    "That's why your parents should've used a condom you disgrace of a human",
    "Uh ha? Say that again pinky dick!?",
    "Get some help retard.",
    "Fucking millennial",
    "No wonder why the new generation is just a bunch of pussies"
]


def send_help():
    """
    Send help!
    :return: A message containing help information.
    """
    return """
```
BigDogg v1.0

Structure: dogg [command] [arg1, arg2, ...]

Commands:
    help    -   Send help (print this message).
    hello   -   Say hello to BigDogg.
    add     -   Add two numbers. This uses two arguments and the two arguments must be either integers or floats.
    sub     -   Subtract two numbers. This uses two arguments and the two arguments must be either integers or floats.
    mul     -   Multiply two numbers. This uses two arguments and the two arguments must be either integers or floats.
    div     -   Divide two numbers. This uses two arguments and the two arguments must be either integers or floats.
    
Criticism dogg [...]:
    Just say a bad work or words to dogg and he will respond. Currently supported ones are,
        "fuck you", "get lost", "suck my dick",
        "your trash", "your mom", "thats what she said",
        "ok boomer", "suck my dick", "fucking nigger"
    
```
     """


def say_hello():
    """
    Return a hello message to be sent.
    :return: The message to be sent.
    """
    return random.choice(hello_list)


def perform_calculation(content, op):
    """
    Performs an operation on a given message. This also returns the error message if something fails.
    :param content: The content.
    :param op: The operation to be performed.
    :return: The result or error.
    """
    input_list = content.split(" ")
    if len(input_list) < 4:
        return "Something is wrong in the command! Make sure that the add command meets the required specification (" \
               "consult `dogg help`). "

    try:
        return str(op(int(input_list[2]), int(input_list[3])))
    except ValueError:
        try:
            return str(op(float(input_list[2]), float(input_list[3])))
        except ValueError:
            return "Hmm... your two arguments are not supported. Make sure that both of the arguments are either " \
                   "integers or floats. "


def perform_addition(content):
    """
    Perform addition by splitting the message and adding the 3rd and 4th argument. Prompt an error if something fails.
    :param content: The input message.
    :return: The result as a string.
    """
    return perform_calculation(content, operator.add)


def perform_subtraction(content):
    """
    Perform subtraction by splitting the message and subtracting the 3rd and 4th argument. Prompts an error if
    something fails.
    :param content: The input message.
    :return: The result as a string.
    """
    return perform_calculation(content, operator.sub)


def perform_multiplication(content):
    """
    Perform multiplication by splitting the message and subtracting the 3rd and 4th argument. Prompts an error if
    something fails.
    :param content: The input message.
    :return: The result as a string.
    """
    return perform_calculation(content, operator.mul)


def perform_division(content):
    """
    Perform subtraction by splitting the message and subtracting the 3rd and 4th argument. Prompts an error if
    something fails.
    :param content: The input message.
    :return: The result as a string.
    """
    return perform_calculation(content, operator.div)


def dogg_bark(content):
    for candidate in bark_candidates:
        if candidate in content:
            return random.choice(bark_list)

    return "Bruhh you don't even know what the commands are. Make sure you check `dogg help` before talking to be fool."


def execute(content):
    """
    Execute a command. By default python single line codes are allowed.
    :param content: The content containing the code.
    :return: The executed result.
    """
