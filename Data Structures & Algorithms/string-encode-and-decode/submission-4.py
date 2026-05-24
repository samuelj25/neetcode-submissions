class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "^"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0

        while r < len(s):
            if s[r] == "^":
                length = int(s[l:r])
                wrd = s[r + 1: r + length + 1]
                res.append(wrd)
                l = r + length + 1
                r = l
            r += 1
        
        return res