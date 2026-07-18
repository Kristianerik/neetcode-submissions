from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        dq = deque([])
        for r in range(len(nums)):
            if dq and dq[0] < l:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if r - l + 1 == k:
                output.append(nums[dq[0]])
                l += 1
                 
        return output