class Solution:

    oneString = ""

    def encode(self, strs: List[str]) -> str:
        for s in strs:
            Solution.oneString = Solution.oneString + s + "{"
        return Solution.oneString
        
    def decode(self, s: str) -> List[str]:
        output = []
        word = ""
        for letter in s:
            if letter != "{":
                word += letter
            else:
                output.append(word)
                word = ""
        Solution.oneString = ""
        return output