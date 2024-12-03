"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
def clone_graph(node: Optional['Node']) -> Optional['Node']:
    lookup = {}

    def helper(node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        if node in lookup:
            return lookup[node]
        lookup[node] = Node(node.val)

        new_neighbors = [ helper(n) for n in node.neighbors ]
        lookup[node].neighbors = new_neighbors
        return lookup[node]
    return helper(node