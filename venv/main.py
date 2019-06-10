from node import *
from Graph import *
from random import *
from cohesion import *

def main():
    graph = Graph(10)
    graph.make_random_conn(5)
    print(graph)

    cohesion = Cohesion()
    cohesion.find_way(0, 4, graph)
    print(cohesion.get_way())


if __name__ == '__main__':
    main()