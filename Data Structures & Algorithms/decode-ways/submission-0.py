class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        one, two = 1, 1

        for i in range(1, len(s)):
            temp = 0
            if s[i] != '0':
                temp = one
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += two
            one, two = temp, one
        
        return one