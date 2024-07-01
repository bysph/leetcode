# @lcpr-before-debug-begin
from python3problem496 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30204
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # 存放缓存数据，避免重复计算
        m = {}
        # 单调栈
        stack = []
        # 遍历nums2，利用单调栈计算每个i的下一个更大元素
        for i in range(len(nums2)-1, -1, -1):
            # 栈底到栈顶是单调递减的，一旦发现新元素比栈顶元素小，就丢弃栈顶元素，直至新元素可以放到栈顶
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                m[nums2[i]] = stack[-1]
            else:
                m[nums2[i]] = -1
            # 将新元素放到栈顶
            stack.append(nums2[i])
        print(m)
        res = []
        for i in nums1:
            res.append(m[i])
        return res



            


# @lc code=end



#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2].\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4].\n
# @lcpr case=end

#
# @lcpr case=start
# [4,1,2]\n[1,3,4,2]\n
# @lcpr case=end

#

