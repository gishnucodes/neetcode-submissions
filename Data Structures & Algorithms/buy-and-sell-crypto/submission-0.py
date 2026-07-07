class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        maxProfit = 0
        for i in range(0,n):

            for j in range(i+1,n):

                val = prices[j]-prices[i]
                if val > maxProfit :
                    maxProfit=val
                
        return maxProfit
        