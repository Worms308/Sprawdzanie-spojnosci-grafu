import math

class Node():

    def __init__(self, x:int, y:int, id:int, connected:[int]):
        self.x = x
        self.y = y
        self.id = id
        self.connections = connected

    def __str__(self):
        return "Node id: {} Coordinates: ({},{})   {}".format(self.id, self.x, self.y, self.get_connections())

    def get_connections(self):
        result = ""
        for it in self.connections:
            result += "\t" + str(it)
        return result + '\n'

    def add_connection(self, id):
        for it in range(self.connections.__len__()):
            if self.connections[it] == id:
                return

        if id != self.id:
            self.connections.append(id)
            self.connections.sort()

    def check_distance(node1, node2):
        return math.sqrt(pow(node2.x - node1.x ,2) + pow(node2.y - node1.y,2))