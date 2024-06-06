#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30203
#
# [337] 打家劫舍 III
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # f1(node) 表示选中 node 时，能够盗取的最高金额
        # f2(node) 表示不选 node 时，能够盗取的最高金额
        # f1(node) = node.val + f2(node.left) + f2(node.right)
        # f2(node) = max(f1(node.left)+f1(node.right), f1(node.left)+f2(node.right), f2(node.left)+f2(node.right), f2(node.left)+f1(node.right))

        def dfs(node):
            if node == None:
                return 0, 0
            res = 0
            if node.left != None:
                
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#

