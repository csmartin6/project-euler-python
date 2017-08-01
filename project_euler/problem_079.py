import sys
from timeit import default_timer as timer
import os
import utils
import networkx as nx


def problem_079():
    filename = os.path.join(os.path.dirname(__file__), '../data/p079_keylog.txt')
    with open(filename, 'r') as f:
        nums = [utils.as_digit_array(int(line.rstrip('\n'))) for line in f]

    G = nx.DiGraph()
    for n in nums:
        for j in n:
            if j not in G:
                G.add_node(j)
        G.add_node(n[0])
        G.add_edge(n[0], n[1])
        G.add_edge(n[1], n[2])

    if not nx.is_directed_acyclic_graph(G):
        return None


    return utils.from_digit_array(nx.topological_sort(G))


def main():
    print("Problem 79")
    start = timer()
    print("Answer: {}".format(problem_079()))
    print("Elapsed time: {}".format(timer() - start))


if __name__ == '__main__':
    sys.exit(main())