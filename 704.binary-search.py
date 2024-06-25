#
# @lc app=leetcode.cn id=704 lang=python3
# @lcpr version=30203
#
# [704] 二分查找
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if (l == r and nums[l] == target):
            return l
        while (r > l):
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
                continue
            elif nums[m] > target:
                r = m
                continue
            else:
                return m
        if nums[l] == target:
            return l
        else:
            return -1


            

# @lc code=end



#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

