class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()
        visited = set()

        output = []

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
            output.append(current)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output
        