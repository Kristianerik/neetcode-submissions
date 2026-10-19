class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[1], cost[0]

        for i in range(2, len(cost)):
            temp = one
            one = cost[i] + min(one, two)
            two = temp

        return min(one, two)