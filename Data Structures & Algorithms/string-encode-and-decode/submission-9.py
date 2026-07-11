class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode = encode + s + "{"
        return encode

    def decode(self, s: str) -> List[str]:
        word = ""
        result = []
        for c in s:
            if c == "{":
                result.append(word)
                word = ""
            else:
                word += c
        return result
