class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def dfs(index, current_subset, curSum):
            if curSum > target: return
            elif curSum == target:
                results.append(current_subset[:])
                return
            
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                dfs(i, current_subset, curSum + nums[i])
                current_subset.pop()
            
        dfs(0, [], 0)
        return results
