class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        destinctChars = set()
        maxLen = 0

        while r < len(s):
            if s[r] not in destinctChars:
                destinctChars.add(s[r])
                if len(destinctChars) > maxLen:
                    maxLen = len(destinctChars)
                r += 1
            else:
                destinctChars.discard(s[l])
                l += 1

        return maxLen
