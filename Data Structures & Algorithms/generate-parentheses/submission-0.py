class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def dfs(openCount, closeCount, current):
            if closeCount == n:
                results.append(current)
                return
            if openCount < n:
                dfs(openCount + 1, closeCount, current + "(")
            if closeCount < openCount:
                dfs(openCount, closeCount  + 1, current + ")")
 
        dfs(0, 0, "")
        return results  