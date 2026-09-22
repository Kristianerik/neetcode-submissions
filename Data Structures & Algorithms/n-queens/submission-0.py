class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        results = []
        cols = set()
        posDiag = set()
        negDiag = set()

        def dfs(row, current_subset):
            if row == n:
                results.append(current_subset[:])
                return

            for c in range(n):
                if c not in cols and (row + c) not in posDiag and (row - c) not in negDiag:
                    row_string = "." * c + 'Q' + "." * (n - c - 1)
                    cols.add(c)
                    posDiag.add(row + c)
                    negDiag.add(row - c)
                    current_subset.append(row_string)
                    dfs(row + 1, current_subset)

                    cols.remove(c)
                    posDiag.remove(row + c)
                    negDiag.remove(row - c)
                    current_subset.pop()

        dfs(0, [])
        return results