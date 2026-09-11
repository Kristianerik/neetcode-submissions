class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(index, current_subset):
            results.append(current_subset[:])
            for i in range(index, len(nums)):
                current_subset.append(nums[i])
                dfs(i+1, current_subset)
                current_subset.pop()
        
        dfs(0, [])
        return results
