class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        minL= prices[0]
        maxProfit = 0

        while r < len(prices):
            if prices[r] < minL:
                minL = prices[r]
            else:
                maxProfit = max(maxProfit, prices[r] - minL)
            r += 1
        
        return maxProfit