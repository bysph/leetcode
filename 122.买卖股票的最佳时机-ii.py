#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 判断是否符合贪心选择性质：相邻两天买入卖出能赚钱，全局利润就最高
        profit = 0
        for i in range(0, len(prices)-1):
            if prices[i] >= prices[i+1]:
                continue
            profit += prices[i+1] - prices[i]
        return profit

# @lc code=end

