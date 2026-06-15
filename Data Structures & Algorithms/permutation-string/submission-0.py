class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1) - 1
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        for i in range(l, r):
            s2_count[ord(s2[i]) - ord('a')] += 1

        while ((l <= r) and (r < len(s2))):
            s2_count[ord(s2[r]) - ord('a')] += 1
            if (s2_count == s1_count):
                return True
            else:
                s2_count[ord(s2[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return False
