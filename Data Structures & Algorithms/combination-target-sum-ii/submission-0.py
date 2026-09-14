class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        candidates.sort()

        def dfs(index, current_subset, curSum):
            if curSum > target: return
            elif curSum == target:
                results.append(current_subset[:])
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]: continue
                current_subset.append(candidates[i])
                dfs(i+1, current_subset, curSum + candidates[i])
                current_subset.pop()
        

        dfs(0, [], 0)
        return results