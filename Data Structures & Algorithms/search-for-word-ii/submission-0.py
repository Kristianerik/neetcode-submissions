class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word

        def dfs(node, row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return
            c = board[row][col]
            if c == "#" or c not in node.children:
                return
            
            nextNode = node.children[c]

            if nextNode.word:
                results.append(nextNode.word)
                nextNode.word = None

            board[row][col] = "#"
            dfs(nextNode, row+1, col)
            dfs(nextNode, row-1,col)
            dfs(nextNode, row, col+1)
            dfs(nextNode, row, col-1)
            board[row][col] = c
        
        results = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(root, r, c)
        
        return results

