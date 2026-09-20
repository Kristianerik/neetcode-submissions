class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []

        def dfs(index, current_partition):
            if index == len(s):
                results.append(current_partition[:])
                return
            for end in range(index + 1, len(s) + 1):
                substring = s[index:end]
                if self.isPalindrome(substring):
                    current_partition.append(substring)
                    dfs(end, current_partition)
                    current_partition.pop()
        
        dfs(0, [])
        return results

    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1;
            j -= 1;

        return True;