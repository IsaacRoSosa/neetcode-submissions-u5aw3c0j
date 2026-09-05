class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProf = 0
        for i in range(1,len(prices)):
            maxProf = max(maxProf, prices[i]- buyPrice)
            buyPrice = min(buyPrice,prices[i])
        return maxProf