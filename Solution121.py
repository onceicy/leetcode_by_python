class Solution121:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = -1
        maxprofit = 0
        for price in prices:
            if minprice == -1 or minprice >price:
                minprice = price
            maxprofit = max(price - minprice, maxprofit)
        return maxprofit
