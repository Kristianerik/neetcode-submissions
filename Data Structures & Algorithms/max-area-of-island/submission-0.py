class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        curArea = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            
            return (1 + 
                dfs(row + 1,col) +
                dfs(row - 1,col) +
                dfs(row,col + 1) +
                dfs(row,col - 1)) 

        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    curArea = dfs(r,c) 
                    if curArea > maxArea:
                        maxArea = curArea

        return maxArea