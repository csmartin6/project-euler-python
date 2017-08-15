import sys
from timeit import default_timer as timer
import os
import numpy as np
import networkx as nx


def problem_083():
    filename = os.path.join(os.path.dirname(__file__), '../data/p083_matrix.txt')
    with open(filename, 'r') as f:
        matrix = np.loadtxt(f, delimiter=",", dtype=int)

    # matrix = np.array([[131, 201, 630, 537, 805],
    #                    [673, 96, 803, 699, 732],
    #                    [234, 342, 746, 497, 524],
    #                    [103, 965, 422, 121, 37],
    #                    [18, 150, 111, 956, 331]]).T

    m, n = matrix.shape

    graph = nx.DiGraph()
    for i in range(0, m):
        for j in range(0, n):
            graph.add_node((i, j))

    graph.add_node("source")
    graph.add_edge("source", (0, 0), {'weight': matrix[0, 0]})
    graph.add_node("target")
    graph.add_edge((m - 1, n-1), "target", {'weight': 0})

    for i in range(0, m):
        for j in range(0, n):
            if i > 0:
                graph.add_edge((i - 1, j), (i, j), {'weight': matrix[i, j]})
            if i < m - 1:
                graph.add_edge((i + 1, j), (i, j), {'weight': matrix[i, j]})
            if j > 0:
                graph.add_edge((i, j - 1), (i, j), {'weight': matrix[i, j]})
            if j < n - 1:
                graph.add_edge((i, j + 1), (i, j), {'weight': matrix[i, j]})

    return nx.shortest_path_length(graph, "source", "target", weight='weight')


def main():
    print("Problem 83")
    start = timer()
    print("Answer: {}".format(problem_083()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())
