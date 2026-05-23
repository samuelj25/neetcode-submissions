class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            curr = prices[i] - prices[i - 1]
            if curr > 0:
                profit += curr

        return profit
                