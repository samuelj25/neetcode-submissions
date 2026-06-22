class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while ((stack) and (temperatures[i] > temperatures[stack[-1]])):
                prev_i = stack.pop()
                res[prev_i] = i - prev_i
            stack.append(i)

        return res
