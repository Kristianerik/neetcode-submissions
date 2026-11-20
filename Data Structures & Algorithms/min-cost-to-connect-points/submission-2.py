class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minDist = [float('inf')] * n
        visited = [False] * n
        minDist[0] = 0
        total = 0

        for _ in range(n):
            u = -1
            for j in range(n):
                if not visited[j] and (u == -1 or minDist[j] < minDist[u]):
                    u = j

            visited[u] = True
            total += minDist[u]

            for j in range(n):
                if not visited[j]:
                    d = abs(points[u][0] - points[j][0]) + abs(points[u][1] - points[j][1])
                    minDist[j] = min(minDist[j], d)

        return total