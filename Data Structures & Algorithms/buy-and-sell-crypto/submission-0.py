class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 101
        high = -1
        profit = 0

        for p in prices:
            if p > high:
                high = p
                profit = max(profit, high - low)
            if p < low:
                low = p
                high = -1 # reset
                
        return profit