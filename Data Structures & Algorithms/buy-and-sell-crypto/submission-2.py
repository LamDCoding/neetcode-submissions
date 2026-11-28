class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #left=buy. right=sell
        maxP = 0

        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r #shift it since right is the lowest price atm and it has be after the lowest so the next highest
            r += 1
        return maxP
