class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 2])
        freshCount = sum(grid[r][c] == 1 for r in range(len(grid)) for c in range(len(grid[0])))
        minutes = 0

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if newR < 0 or newC < 0 or newR >= len(grid) or newC >= len(grid[0]):
                        continue
                    if grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        freshCount -= 1
                        queue.append((newR, newC))
                    
            minutes += 1
        
        return -1 if freshCount > 0 else max(0, minutes - 1)
