class Solution:
    def solve(self, board: List[List[str]]) -> None:
        queue = deque()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1) and board[r][c] == 'O':
                    queue.append((r,c))
                    board[r][c] = 'S'
        

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if newR < 0 or newC < 0 or newR >= len(board) or newC >= len(board[0]):
                    continue

                if board[newR][newC] != 'O':
                    continue

                board[newR][newC] = 'S'
                queue.append((newR,newC))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] = 'O'