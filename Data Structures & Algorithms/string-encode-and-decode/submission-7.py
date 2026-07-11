class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for s in strs:
            encode = encode + s + "{"
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        word = ""
        for c in s:
            if c == "{":
                decode.append(word)
                word = ""
            else:
                word += c
        return decode

