class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            for c in s:
                encode = encode + c
            encode = encode + "{"
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        word = ""
        for c in s:
            if c == "{":
                decode.append(word)
                word = ""
            else:
                word = word + c
        return decode
