class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)

        result = []

        def dfs(airport):
            while adj[airport]:
                dfs(adj[airport].pop())
            result.append(airport)
        
        dfs("JFK")
        return result[::-1]
              