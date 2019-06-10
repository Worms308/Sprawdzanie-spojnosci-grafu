from random import *
from typing import List

from node import Node


class Graph:

    def __init__(self, num_of_elements):
        self.nodes = []
        for it in range(num_of_elements):
            self.nodes.append(Node(randrange(20), randrange(20), it, []))

    def make_random_conn(self, max_connections: int):
        for it in self.nodes:
            node_num = randrange(max_connections)
            for it2 in range(node_num):
                it.add_connection(randrange(self.nodes.__len__()))

    def __str__(self):
        result = ""
        for it in self.nodes:
            result += str(it)
        return result

    def get_neighbours(self, id: int) -> List:
        return self.nodes[id].connections

    def get_node(self, id: int):
        return self.nodes[id]

