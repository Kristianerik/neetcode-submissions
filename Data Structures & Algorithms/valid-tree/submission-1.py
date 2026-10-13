class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adj = {i: [] for i in range(n)}
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(current, parent):
            if current in visited:
                return False
            
            visited.add(current)

            for neighbor in adj[current]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, current):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n




