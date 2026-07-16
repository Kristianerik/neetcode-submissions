class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        chars = [0] * 26
        nonZero = 0

        for c in s1:
            chars[ord(c) - ord('a')] += 1
        nonZero = sum(1 for x in chars if x != 0)

        l = 0
        for r in range(len(s2)):
            idx = ord(s2[r]) - ord('a')
            chars[idx] -= 1
            if chars[idx] == 0:
                nonZero -= 1
            elif chars[idx] == -1:
                nonZero += 1
            
            if r - l + 1 == window:
                if nonZero == 0:
                    return True
                idx = ord(s2[l]) - ord('a')
                chars[idx] += 1
                if chars[idx] == 0:
                    nonZero -= 1
                elif chars[idx] == 1:
                    nonZero += 1
                l += 1
        
        return False


        