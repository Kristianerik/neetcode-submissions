class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()
        visited = set()

        def dfs(current):
            if current in visited:
                return True
            if current in visiting:
                return False

            visiting.add(current)

            for neighbor in adj[current]:
                if not dfs(neighbor):
                    return False
            
            visiting.remove(current)
            visited.add(current)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True