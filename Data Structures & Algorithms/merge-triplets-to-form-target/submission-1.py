class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(target)
        maxTrips = []

        for i in range(n):
            curMax = 0
            for j in range(len(triplets)):
                if all(triplets[j][k] <= target[k] for k in range(n)):
                    curMax = max(curMax, triplets[j][i])
            maxTrips.append(curMax)   

        m = len(maxTrips) 
        for i in range(m):
            if maxTrips[i] != target[i]:
                return False
        
        return True