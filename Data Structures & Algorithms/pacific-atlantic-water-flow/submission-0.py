class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        pacQueue = deque()
        atlQueue = deque()


        for c in range(len(heights[0])):
            pacific.add((0, c))
            pacQueue.append((0,c))
            atlantic.add((len(heights)- 1, c))
            atlQueue.append((len(heights)- 1, c))

        for r in range(len(heights)):
            pacific.add((r, 0))
            pacQueue.append((r, 0))
            atlantic.add((r, len(heights[0])- 1))
            atlQueue.append((r, len(heights[0])- 1))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc

                    if newR < 0 or newC < 0 or newR >= len(heights) or newC >= len(heights[0]): 
                        continue
                    if (newR, newC) in visited:
                        continue
                    if heights[newR][newC] < heights[r][c]:
                        continue
                    
                    visited.add((newR, newC))
                    queue.append((newR, newC))

        bfs(pacQueue, pacific)
        bfs(atlQueue, atlantic)
        return [list(cell) for cell in pacific & atlantic]
