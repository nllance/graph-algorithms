#!/usr/bin/env python3

from graphs import *
from random import randint
import math
import matplotlib.pyplot as plt

# Create a random graph with k nodes and c edges
def create_random_graph(k: int, c: int) -> Graph:
    G = Graph(k)
    while c > 0:
        a = randint(0, k - 1)
        b = randint(0, k - 1)
        if (a == b) or (G.are_connected(a, b)):
            continue
        G.add_edge(a, b)
        c -= 1

    return G

# Test the relationship between portion of cyclic graphs and number of edges c
# Result: c = 55 (half), c = 75 (almost all)
def cycle_test():
    # Number of edges c from 0 to 500
    cs = [_ for _ in range(501)]
    ys = []

    for c in cs:
        # Test each c 100 times to calculate portion
        result = 0
        for _ in range(100):
            # Number of nodes k = 100
            G = create_random_graph(100, c)
            if has_cycle(G):
                result += 1
        ys.append(result)

    plt.plot(cs, ys, '.')
    plt.xlabel("Number of edges c")
    plt.ylabel("Portion of cyclic graphs (%)")
    plt.title("The portion of cyclic graphs vs number of edges c")
    plt.show()

# Test the relationship between portion of fully connected graphs and number of edges c
# Result: c = 160 (always 0), c = 245 (half), c = 450 (almost all)
def connected_test():
    # Number of edges c from 0 to 500
    cs = [_ for _ in range(501)]
    ys = []

    for c in cs:
        # Test each c 100 times to calculate portion
        result = 0
        for _ in range(100):
            # Number of nodes k = 100
            G = create_random_graph(100, c)
            if is_connected(G):
                result += 1
        ys.append(result)

    plt.plot(cs, ys, '.')
    plt.xlabel("Number of edges c")
    plt.ylabel("Portion of fully connected graphs (%)")
    plt.title("The portion of fully connected graphs vs number of edges c")
    plt.show()

cycle_test()
connected_test()
