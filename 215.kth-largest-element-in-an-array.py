#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30203
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = []
        heapq.heapify(l)
        for n in nums:
            heapq.heappush(l, -n)
        for i in range(0, k-1):
            v = heapq.heappop(l)
        res = -heapq.heappop(l)
        return res

# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

