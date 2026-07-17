class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        tChars = {}
        for c in t:
            tChars[c] = tChars.get(c, 0) + 1
        
        windowChars = {}
        have = 0
        need = len(tChars)  
        output = ""
        minLen = float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            windowChars[c] = windowChars.get(c, 0) + 1
            
            if c in tChars and windowChars[c] == tChars[c]:
                have += 1

            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    output = s[l:r+1]

                windowChars[s[l]] -= 1
                if s[l] in tChars and windowChars[s[l]] < tChars[s[l]]:
                    have -= 1
                l += 1

        return output
