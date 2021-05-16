import random
import operator

hello_candidates = [
    "heyy", "hey",
    "hello"
]

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


def add_to_list(list_name, list_to_add, content, begin_index):
    """
    Add a new element to a list.
    :param list_name: The name of the list.
    :param list_to_add: The list to add the element to.
    :param content: The input message.
    :param begin_index: The beginning index of the entry in the list.
    :return: The return statement.
    """
    input_list = content.split()

    if len(input_list) < (begin_index + 1):
        return f"Hmm... I think you forgot to enter what you want to add. Please follow the format 'dogg add {list_name} list [...]'"

    entry_to_append = ""
    for word in range(begin_index, len(input_list)):
        entry_to_append += input_list[word] + " "

    list_to_add.append(entry_to_append)

    return f"New entry appended to the {list_name} list: " + entry_to_append


def remove_from_list(list_name, list_to_be_removed_from, content, begin_index):
    """
    Remove an entry from a list.
    :param list_name: The name of the list.
    :param list_to_be_removed_from: The list to remove the element from.
    :param content: The message.
    :param begin_index: The begin index of the entry.
    :return: The return note.
    """
    input_list = content.split()

    if len(input_list) < (begin_index + 1):
        return f"Hmm... I think you forgot to enter what you want to remove. Please follow the format 'dogg remove from {list_name} list [...]'"

    entry_to_remove = ""
    for word in range(begin_index, len(input_list)):
        entry_to_remove += input_list[word] + " "

    try:
        list_to_be_removed_from.remove(entry_to_remove)

    except ValueError:
        return f"I think the entry you wish to remove isn't there in the list. Are you sure about that? Maybe use `dogg print {list_name} list` command before issuing this command."

    return f"The element is successfully removed from the {list_name} list."


def print_list(list_name, list_to_print):
    """
    Print all the contents of a list.
    :param list_name: The name of the list.
    :param list_to_print: The list to be printed.
    :return: The string to be submitted to the user.
    """
    string = ""
    for entry in list_to_print:
        string += entry + "\n"

    return f"""
Printing {list_name} list.
```
{string}
```
"""


def wrong_command():
    """
    Issue a note if a wrong command is set.
    :return: The issue note.
    """
    return "Wrong command dumb ass. Go check `dogg help` before coming back moron."


def send_help():
    """
    Send help!
    :return: A message containing help information.
    """
    return f"""
```
BigDogg v1.0

Commands: dogg [command] [arg1, arg2, ...]
    help                -   Send help (print this message).
    hello               -   Say hello to BigDogg.
    add                 -   Add two numbers. This uses two arguments and the two arguments must be either integers or floats.
    sub                 -   Subtract two numbers. This uses two arguments and the two arguments must be either integers or floats.
    mul                 -   Multiply two numbers. This uses two arguments and the two arguments must be either integers or floats.
    div                 -   Divide two numbers. This uses two arguments and the two arguments must be either integers or floats.
    enable chat bot     -   Enable chat bot and talk to Big Dogg.
    disable chat bot    -   Disable chat bot.
    all commands        -   Print all the supported commands.
    
Author specific commands: dogg [command] [entry...]
    add to hello list                       -   Add a new element to the hello response list.
    remove from hello list                  -   Remove an element from the hello response list.
    add to hello candidate list             -   Add a new element to the hello candidate (selection) list. 
    remove from hello candidate list        -   Remove an element from the hello candidate (selection) list.
    add to bark list                        -   Add a new element to the bark response list.
    remove from bark list                   -   Remove an element from the bark response list.
    add to bark candidate list              -   Add a new element to the bark candidate (selection) list.
    remove from bark candidate list         -   Remove an element from the bark candidate (selection) list.
```
     """


def print_all_commands():
    """
    Print all the available commands.
    :return: The commands.
    """
    criticism_string = ""
    for entry in bark_candidates:
        criticism_string += "\t\t" + entry + "\n"

    hello_string = ""
    for entry in hello_candidates:
        hello_string += "\t\t" + entry + "\n"

    return f"""
```
All commands:
    Friendly: dogg [...]
{hello_string}
    Criticism: dogg [...]
{criticism_string}
    Execute: 
        Execute a code snippet using big dogg. There are 2 ways to execute code.
        1. Using a file attachment.
            For this the syntax is pretty simple. Add an attachment and add 'dogg execute' in the description.
        
        2. Using code blocks.
            This is a little different from the 1st one, you need to say whats the language type. You can typically do it like this:
                dogg execute
                `` `python
                print("Fuck you")
                `` `
                
                
            And remember, it should be as one file so make sure to press shift before breaking the line.
            No, BigDogg doesnt take inputs, for now.
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

    return "Bruhh you don't even know what the commands are. Make sure you check `dogg help` before talking to me fool."
