"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        start_node = Node(node.val)
        hashmap = {node: start_node}
        queue = deque([node])
        while queue:
            original = queue.popleft()
            for neighbor in original.neighbors:
                if neighbor not in hashmap:
                    cloned = Node(neighbor.val)
                    hashmap[neighbor] = cloned
                    queue.append(neighbor)
                hashmap[original].neighbors.append(hashmap[neighbor])
            
        return start_node