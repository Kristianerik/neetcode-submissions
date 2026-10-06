class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque([(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR >= len(grid) or newC >= len(grid[0]):
                    continue
                if grid[newR][newC] == 2147483647:
                    grid[newR][newC] = grid[r][c] + 1
                    queue.append((newR, newC))