class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((v,t))

        heap = [(0, k)]
        visited = set()
        result = 0

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited: 
                continue
            
            visited.add(node)
            result = time

            for nei, t in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (time + t, nei))
        
        return result if len(visited) == n else -1