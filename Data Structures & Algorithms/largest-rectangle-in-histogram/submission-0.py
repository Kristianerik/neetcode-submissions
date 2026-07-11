class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, num in enumerate(heights):
            start = i
            while stack and num < stack[-1][1]:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i-idx))
                start = idx
            
            stack.append((start, num))
        
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        
        return maxArea
