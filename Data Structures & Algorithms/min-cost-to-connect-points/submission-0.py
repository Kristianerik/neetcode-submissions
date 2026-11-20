class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        heap = [(0, 0)]
        visited = set()
        total = 0

        while len(visited) < n:
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            total += cost

            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (nei_cost, nei))
        
        return total