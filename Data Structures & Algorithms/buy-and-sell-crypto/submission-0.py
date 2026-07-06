class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_p = float("inf")
        highest_profile = -float("inf")

        for i, p in enumerate(prices):

            # find the lowest from the left
            # find the highest profit

            lowest_p = min(p, lowest_p)
            profit = p - lowest_p
            highest_profile = max(highest_profile, profit)
        
        return highest_profile
