class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = [1] + digits
        i = len(res) - 1

        while (i > 0):
            if (res[i] != 9):
                res[i] += 1
                break
            else:
                res[i] = 0
                i -= 1
        return res if i == 0 else res[1:]
