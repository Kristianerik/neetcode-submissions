class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            t, r, c = heapq.heappop(heap)

            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                if (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))

