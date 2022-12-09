# graph with graph
graph = {}


# Node Class
class Node:
    # Array to store all objects
    nodes = []

    # Constructor
    def __init__(self, name: str, topic: bool = False):
        self.name = name
        self.topic = topic
        self.nodes.append(self)

    # Function to add friends
    def add_friends(self, *values):
        try:
            # Check if the user is in the graph
            graph[self].add(*values)
        except KeyError:
            # If not, add the user to the graph
            graph[self] = {*values}

    # Function to remove friend
    def delete_friends(self, friend: str):
        graph[self].remove(friend)

    # Static function to display all objects
    @classmethod
    def all_objects(self):
        return self.nodes

    # Function to print object
    def __str__(self):
        return self.name
