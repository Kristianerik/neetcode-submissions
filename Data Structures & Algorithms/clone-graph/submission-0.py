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
            return None
        visited = {}

        def dfs(cur):
            if not cur:
                return

            if cur in visited:
                return visited[cur]
            else:
                clone = Node(cur.val, [])
                visited[cur] = clone
                for neighbor in cur.neighbors:
                    clone.neighbors.append(dfs(neighbor))

                return clone

        dfs(node)
        return visited[node]
