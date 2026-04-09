class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        min_till_now = 1000
        for i in prices:
            min_till_now = min(min_till_now,i)
            prof = max(prof,i - min_till_now)

        return prof
        
        