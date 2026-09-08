class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        res = 0

        while ((l <= r) and (r < len(s))):
            if (s[r] not in seen):
                seen.add(s[r])
                r += 1
                res = max(res, r - l)
            else:
                while (s[r] in seen):
                    seen.remove(s[l])
                    l += 1
        
        return res
