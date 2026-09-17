class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []

        nums.sort()
        def dfs(index, current_subset):
            results.append(current_subset[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current_subset.append(nums[i])
                dfs(i+1, current_subset)
                current_subset.pop()

        dfs(0, [])
        return results