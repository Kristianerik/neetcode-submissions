class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        charCount = {}
        maxLen = 0
        mostFreq = 0

        while r < len(s):
            charCount[s[r]] = charCount.get(s[r], 0) + 1
            mostFreq = max(charCount.values())
            
            if (r - l + 1) - mostFreq <= k:    
                maxLen = max(maxLen, r - l + 1)
                r += 1
            else:
                charCount[s[l]] -= 1
                l += 1
                r += 1

        return maxLen