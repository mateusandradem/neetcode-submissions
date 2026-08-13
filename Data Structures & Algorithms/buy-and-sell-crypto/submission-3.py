class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = max(prices)
        max_profit = 0

        while len(prices) > 1:
            max_p_idx = prices.index(max_price)
            if max_p_idx != 0:
                min_price = min(prices[:max_p_idx])
                max_profit = max(max_price - min_price, max_profit)

            prices.remove(max_price)
            max_price = max(prices)

        return max_profit