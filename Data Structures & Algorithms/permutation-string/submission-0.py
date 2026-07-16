class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        l = 0
        r = 0
        chars = [0] * 26
        charsTwo = [0] * 26

        for c in s1:
            chars[ord(c) - ord('a')] += 1
        
        while r < len(s2):
            # add new right character
            charsTwo[ord(s2[r]) - ord('a')] += 1
            
            if chars == charsTwo:
                return True
            
            # window is full, slide forward
            if r - l + 1 == window:
                charsTwo[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            r += 1
        
        return False


        