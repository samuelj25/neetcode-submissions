class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        max_length = 0

        while ((l <= r) and (r < len(s))):
            if (s[r] not in seen):
                seen.add(s[r])
                r += 1
            else: # we have seen s[r]
                max_length = max(max_length, r - l)
                while (s[r] in seen):
                    seen.remove(s[l])
                    l += 1
            max_length = max(max_length, r - l)
            
        return max_length