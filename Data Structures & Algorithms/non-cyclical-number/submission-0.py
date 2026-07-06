class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = 0

        while (n != 1):
            while (n != 0):
                curr += (n % 10) ** 2
                n //= 10
            if (curr in seen):
                return False
            seen.add(curr)
            n = curr
            curr = 0
        return True
