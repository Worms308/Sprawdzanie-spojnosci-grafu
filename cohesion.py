from Graph import *


class Cohesion():
    visited = []
    possible_way = []
    src: int
    dst: int

    def find_way(self, start: int, destiny: int, graph: Graph):
        if self.visited.__len__() == 0:
            self.src = start
            self.dst = destiny
        if start == destiny:
            self.visited.append(start)
            self.possible_way.append(start)
            return
        if start in self.visited or (self.possible_way.__len__() > 0 and self.possible_way[self.possible_way.__len__()-1]) == destiny:
            return
        self.visited.append(start)
        self.possible_way.append(start)
        neighbours = graph.get_neighbours(start)
        if neighbours.__len__() == 0:
            self.possible_way.pop()
        for it in neighbours:
            if it not in self.visited:
                self.find_way(it, destiny, graph)

    def get_way(self):
        if self.src == self.possible_way[0] and self.dst == self.possible_way[self.possible_way.__len__()-1]:
            return self.possible_way
        else:
            return [self.src]
