class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        #DP approach
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True


        def dfs(index, current_partition):
            if index == len(s):
                results.append(current_partition[:])
                return
            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]
                if dp[index][end-1]:
                    current_partition.append(substring)
                    dfs(end, current_partition)
                    current_partition.pop()
        
        dfs(0, [])
        return results
