class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        coins.sort()
        for ele in coins:
            if ele<len(dp) and ele!=0:
                dp[ele] = 1
        for i in range(coins[0],amount+1):
            for ele in coins:
                if i-ele>0:
                    dp[i] = min(dp[i-ele]+1,dp[i])
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
