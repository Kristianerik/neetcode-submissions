class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        numsSet = set()
        for number in nums:
            if number in numsSet:
                return True
            numsSet.add(number)
        return False