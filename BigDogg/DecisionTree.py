from Callbacks import *


class Node:
    node_entry = ""
    callback = None
    next_nodes = None

    def __init__(self, node_entry, callback=wrong_command_callback):
        self.node_entry = node_entry
        self.callback = callback
        self.next_nodes = {}

    def add_child(self, node_name, node_data):
        self.next_nodes[node_name] = node_data
        return self.next_nodes[node_name]

    def get_child(self, node_name):
        return self.next_nodes[node_name]


class DecisionTree:
    root_node: Node = None

    def populate_add_nodes(self):
        add_node = self.root_node.add_child("add", Node("add"))
        to_node = add_node.add_child("to", Node("to"))
        to_node.add_child("hello list", Node("hello list", add_to_hello_list_callback))
        to_node.add_child("hello candidate list", Node("hello candidate list", add_to_hello_candidate_list_callback))
        to_node.add_child("bark list", Node("bark list", add_to_bark_list_callback))
        to_node.add_child("bark candidate list", Node("bark candidate list", add_to_bark_candidate_list_callback))

    def populate_remove_nodes(self):
        remove_node = self.root_node.add_child("remove", Node("remove"))
        from_node = remove_node.add_child("from", Node("from"))
        from_node.add_child("hello list", Node("hello list", remove_from_hello_list_callback))
        from_node.add_child("hello candidate list", Node("hello candidate list", remove_from_hello_candidate_list_callback))
        from_node.add_child("bark list", Node("bark list", remove_from_bark_list_callback))
        from_node.add_child("bark candidate list", Node("bark candidate list", remove_from_bark_candidate_list_callback))

    def populate_print_nodes(self):
        print_node = self.root_node.add_child("remove", Node("remove"))
        print_node.add_child("hello list", Node("hello list", print_hello_list_callback))
        print_node.add_child("hello candidate list", Node("hello candidate list", print_hello_candidate_list_callback))
        print_node.add_child("bark list", Node("bark list", print_bark_list_callback))
        print_node.add_child("bark candidate list", Node("bark candidate list", print_bark_candidate_list_callback))

    def populate_chat_bot(self):
        chat_bot_node = self.root_node.add_child("chat bot", Node("chat bot"))
        chat_bot_node.add_child("enable", Node("enable", enable_chat_bot_callback))
        chat_bot_node.add_child("disable", Node("disable", disable_chat_bot_callback))

    def populate_execute(self):
        execute_node = self.root_node.add_child("execute", Node("execute"))
        execute_node.add_child("attachments", Node("attachments", execute_attachments_callback))
        execute_node.add_child("block", Node("block", execute_block_callback))

    def populate_hello(self):
        for entry in hello_candidates:
            self.root_node.add_child(entry, Node(entry, say_hello_callback))

    def __init__(self):
        self.root_node = Node("dogg")
        self.root_node.add_child("help", Node("help", send_help_callback))
        self.root_node.add_child("all commands", Node("all commands", print_all_commands_callback))
        self.root_node.add_child("add", Node("add", perform_addition_callback))
        self.root_node.add_child("sub", Node("sub", perform_subtraction_callback))
        self.root_node.add_child("mul", Node("mul", perform_multiplication_callback))
        self.root_node.add_child("div", Node("div", perform_division_callback))

        self.populate_add_nodes()
        self.populate_remove_nodes()
        self.populate_print_nodes()
        self.populate_chat_bot()
        self.populate_execute()
        self.populate_hello()

    def travel_tree(self, parent_list) -> Node:
        final_node = None
        for node in parent_list:
            final_node = self.root_node.get_child(node)

        return final_node

    def add_node_to_tree(self, parent_string, node_name, callback=wrong_command_callback):
        self.travel_tree(parent_string.split(" ")).add_child(node_name, Node(node_name, callback))

    def get_callback(self, node_string):
        return self.travel_tree(node_string.split(" ")).callback
