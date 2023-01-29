class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        DP=[float('inf')]*(amount+1)
        DP[0]=0
        
        for i in range(amount+1):
            for c in coins:
                if i-c>=0:
                    DP[i]=min(DP[i],DP[i-c]+1)
        return DP[amount] if DP[amount]!=float('inf') else -1