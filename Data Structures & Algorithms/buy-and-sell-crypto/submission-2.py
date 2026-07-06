class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_p = prices[0]
        highest_profile = 0

        for i, p in enumerate(prices):
            # find the lowest from the left
            # find the highest profit

            lowest_p = min(p, lowest_p)
            profit = p - lowest_p
            highest_profile = max(highest_profile, profit)

        return highest_profile
