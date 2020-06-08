# 518. Coin Change 2 - Medium
# Tags - Dynamic Programming (DP) (There were no tags mentioned on LC by default)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        n  = len(coins)
        for i in range(n):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]