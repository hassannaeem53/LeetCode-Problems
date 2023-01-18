class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        #prices=prices[::-1]
        #[7 1 5 3 6 4]
        sell,buy=1,0
        while sell<len(prices):
            plus=prices[sell]-prices[buy]
            if prices[sell]>prices[buy]:
                if plus > profit:
                    profit=plus
            else:
                buy=sell
            sell+=1
        return profit