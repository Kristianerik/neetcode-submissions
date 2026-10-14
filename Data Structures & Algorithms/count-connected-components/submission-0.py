class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components = 0
        adj = {i: [] for i in range(n)}
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def dfs(current):
            if current in visited:
                return
            
            visited.add(current)
            for neighbor in adj[current]:
                dfs(neighbor)
        
        for node in range(n):
            if node not in visited:
                components += 1
                dfs(node)
        
        return components