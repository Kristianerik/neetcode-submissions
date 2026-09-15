class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def dfs(current_subset):
            if len(current_subset) == len(nums):
                results.append(current_subset[:])

            for i in range(len(nums)):
                if nums[i] not in current_subset:
                    current_subset.append(nums[i])
                    dfs(current_subset)
                    current_subset.pop()

        dfs([])
        return results