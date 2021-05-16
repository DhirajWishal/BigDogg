from Callbacks import *


class Node:
    node_entry = ""
    callback = None
    next_nodes = None
    node_description = ""

    def __init__(self, node_entry, callback=wrong_command_callback, description=""):
        self.node_entry = node_entry
        self.callback = callback
        self.next_nodes = {}
        self.node_description = description

    def add_child(self, node_name, node_data):
        for key, value in self.next_nodes.items():
            if key in node_name:
                value = node_data
                return value

        self.next_nodes[node_name] = node_data
        return self.next_nodes[node_name]

    def get_child(self, node_name):
        for key, value in self.next_nodes.items():
            if key in node_name:
                return value

        return self.add_child(node_name, Node(node_name))

    def print(self, append_string, indent_factor=0):
        indent_factor += 1
        append_string += (self.node_entry + "\t" + self.node_description + "\n")
        for key, value in self.next_nodes.items():
            append_string = value.print(append_string + ("\t\t" * indent_factor), indent_factor)

        return append_string


class DecisionTree:
    root_node: Node = None

    def populate_add_nodes(self):
        add_node = self.root_node.add_child("add", Node("add"))
        to_node = add_node.add_child("to", Node("to"))

        hello_node = to_node.add_child("hello", Node("hello"))
        hello_node.add_child("list", Node("list", add_to_hello_list_callback, "-Add an element to the hello list."))
        hello_node.add_child("candidate", Node("candidate", add_to_hello_candidate_list_callback, "Add am element to "
                                                                                                  "the hello "
                                                                                                  "candidate list."))

        bark_node = to_node.add_child("bark", Node("bark"))
        bark_node.add_child("list", Node("list", add_to_bark_list_callback, "-Add an element to the bark list."))
        bark_node.add_child("candidate", Node("candidate", add_to_bark_candidate_list_callback, "Add an element to "
                                                                                                "the bark candidate "
                                                                                                "list."))

    def populate_remove_nodes(self):
        remove_node = self.root_node.add_child("remove", Node("remove"))
        from_node = remove_node.add_child("from", Node("from"))

        hello_node = from_node.add_child("hello", Node("hello"))
        hello_node.add_child("list", Node("list", remove_from_hello_list_callback, "-Remove an element from the hello "
                                                                                   "list."))
        hello_node.add_child("candidate", Node("candidate", remove_from_hello_candidate_list_callback, "-Remove an "
                                                                                                       "element from "
                                                                                                       "the hello "
                                                                                                       "candidate "
                                                                                                       "list."))

        bark_node = from_node.add_child("bark", Node("bark"))
        bark_node.add_child("list", Node("list", remove_from_bark_list_callback, "-Remove an element from the bark "
                                                                                 "list. "
                                         ))
        bark_node.add_child("candidate", Node("candidate", remove_from_bark_candidate_list_callback, "-Remove an "
                                                                                                     "element from "
                                                                                                     "the bark "
                                                                                                     "candidate "
                                                                                                     "list."))

    def populate_print_nodes(self):
        print_node = self.root_node.add_child("print", Node("print"))

        hello_node = print_node.add_child("hello", Node("hello"))
        hello_node.add_child("list", Node("list", print_hello_list_callback, "-Print all the elements in the hello "
                                                                             "list. "
                                          ))
        hello_node.add_child("candidate", Node("candidate", print_hello_candidate_list_callback, "-Print all the "
                                                                                                 "elements in the "
                                                                                                 "hello candidate "
                                                                                                 "list."))

        bark_node = print_node.add_child("bark", Node("bark"))
        bark_node.add_child("list", Node("list", print_bark_list_callback, "-Print all the elements in the bark list."))
        bark_node.add_child("candidate", Node("candidate", print_bark_candidate_list_callback, "-Print all the "
                                                                                               "elements in the bark "
                                                                                               "candidate list."))

    def populate_chat_bot(self):
        self.root_node.add_child("unleash", Node("unleash", enable_chat_bot_callback, "-Enable chat bot."))
        self.root_node.add_child("leash", Node("leash", disable_chat_bot_callback, "-Disable chat bot."))

    def populate_execute(self):
        execute_node = self.root_node.add_child("execute", Node("execute"))
        execute_node.add_child("attachments", Node("attachments", execute_attachments_callback, "-Execute one ore more "
                                                                                                "attachments."))
        execute_node.add_child("block", Node("block", execute_block_callback, "-Execute a block of code."))

    def populate_hello(self):
        for entry in hello_candidates:
            self.root_node.add_child(entry, Node(entry, say_hello_callback))

    def __init__(self, tree_name):
        self.root_node = Node(tree_name, description="-The root node of the decision tree.")
        self.root_node.add_child("help", Node("help", send_help_callback, "-Print the help screen."))
        self.root_node.add_child("add", Node("add", perform_addition_callback, "-Add two numbers."))
        self.root_node.add_child("sub", Node("sub", perform_subtraction_callback, "-Subtract two numbers."))
        self.root_node.add_child("mul", Node("mul", perform_multiplication_callback, "-Multiply two numbers."))
        self.root_node.add_child("div", Node("div", perform_division_callback, "-Divide two numbers."))

        add_node = self.root_node.add_child("all", Node("all", print_all_commands_callback, "-A node which supports "
                                                                                            "printing all commands."))
        add_node.add_child("commands", Node("commands", print_all_commands_callback, "-Print all available commands."))

        self.populate_add_nodes()
        self.populate_remove_nodes()
        self.populate_print_nodes()
        self.populate_chat_bot()
        self.populate_execute()
        self.populate_hello()

    def travel_tree(self, parent_list) -> Node:
        if len(parent_list) == 0:
            return self.root_node

        final_node = self.root_node.get_child(parent_list.pop(0))
        for node in parent_list:
            final_node = final_node.get_child(node)

        return final_node

    def add_node_to_tree(self, parent_string, node_name, callback=wrong_command_callback):
        self.travel_tree(parent_string.split(" ")).add_child(node_name, Node(node_name, callback))

    def get_callback(self, node_string):
        split_input = node_string.split(" ")

        for split in split_input:
            if split.lower() == "dogg":
                split_input.remove(split)
                break

        return self.travel_tree(split_input).callback

    def print_all_nodes(self):
        description_string = self.root_node.print("Decision Tree v1.0\n```\n")

        description_string += "\n```"
        return description_string
