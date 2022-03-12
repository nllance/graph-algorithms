#!/usr/bin/env python3

from lab7 import *
from typing import Dict, List
from collections import deque

# Breadth First Search, returns the path from src to dst as a list of nodes
def BFS2(G: Graph, src: int, dst: int) -> List[int]:
    Q = deque([src]) # a queue
    marked = {node : False for node in G.adj}
    marked[src] = True
    # To record path in form of {node: [path from src to node]... }
    path = {src : [src]}

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                path[node] = path[current_node] + [node]
    # If dst is not connected to src
    if dst not in path:
        return []
    return path[dst]

# Depth First Search, returns the path from src to dst as a list of nodes
def DFS2(G: Graph, src: int, dst: int) -> List[int]:
    S = deque([src]) # A stack
    marked = {node : False for node in G.adj}
    path = {src : [src]}

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)
                if (not marked[node]) and (node not in path):
                    path[node] = path[current_node] + [node]
    # If dst is not connected to src
    if dst not in path:
        return []
    return path[dst]

# Breadth First Search, finds a path to every node (which there is a path to)
# and returns these paths in the form of a "predecessor dictionary"
def BFS3(G: Graph, src: int) -> Dict[int, int]:
    Q = deque([src]) # a queue
    marked = {node : False for node in G.adj}
    marked[src] = True
    # To record path in form of {node: previous node... }
    pred = {}

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                pred[node] = current_node
    return pred

# Depth First Search, finds a path to every node (which there is a path to)
# and returns these paths in the form of a "predecessor dictionary"
def DFS3(G: Graph, src: int) -> Dict[int, int]:
    S = deque([src]) # A stack
    marked = {node : False for node in G.adj}
    pred = {}

    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                S.append(node)
                if (not marked[node]) and (node not in pred):
                    pred[node] = current_node
    return pred

# Return True iff there is a cycle in G
def has_cycle(G: Graph) -> bool:
    # All nodes in the graph
    nodes = list(G.adj.keys())
    marked = {node : False for node in G.adj}
    # Call the recursive helper function to detect cycle in different DFS trees
    for node in nodes:
        if not marked[node]:
            # Subgraph starting from current node
            # Parent does not exist, use -1 to represent
            if has_cycle_helper(G, node, marked, -1):
                return True
    return False

# Return iff there is a cycle in subgraph reachable from a certain node
def has_cycle_helper(G: Graph, node: int, marked: Dict[int, bool], parent: int) -> bool:
    marked[node] = True
    # All the nodes djacent to this node
    for adj in G.adj[node]:
        if not marked[adj]:
            if has_cycle_helper(G, adj, marked, node):
                return True
        # If an adjacent node is visited and not parent of the current node
        # Then there is a cycle
        elif parent != adj:
            return True
    return False

# Return True iff there is a path between any two nodes in G
def is_connected(G: Graph) -> bool:
    n = G.number_of_nodes()
    # No edge in the graph
    if n == 0:
        return False
    # Nodes reachable from node 0
    # If the graph has a path between any two nodes, all other nodes should be reachable
    connected = BFS3(G, 0)
    if len(connected) + 1 == n:
        return True
    return False
