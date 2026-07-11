class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Input: array nums [2,20,4,10,3,4,5]
        #MAP {num, count}
        #
        seen = set(nums)
        maxCon = 0
        for num in seen:
            if num - 1 not in seen:
                length = 1
                while num + length in seen:
                    length += 1
                maxCon = max(maxCon, length)
        return maxCon
        #Return len(max(conSeq))