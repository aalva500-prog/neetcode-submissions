class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0
        lowestPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]            
            if (prices[i] - lowestPrice) > maxProf:
                maxProf = prices[i] - lowestPrice
        return maxProf