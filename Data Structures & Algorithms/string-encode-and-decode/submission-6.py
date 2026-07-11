class Solution:

    def encode(self, strs: List[str]) -> str:
        oneString = ""
        for s in strs:
            oneString = oneString + s + "{"
        return oneString
        
    def decode(self, s: str) -> List[str]:
        output = []
        word = ""
        for letter in s:
            if letter != "{":
                word += letter
            else:
                output.append(word)
                word = ""
        return output