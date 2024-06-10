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
        # r(node) 表示选中 node 时，能够盗取的最高金额
        # l(node) 表示不选 node 时，能够盗取的最高金额
        # r(node) = node.val + s(node.left) + s(node.right)
        # s(node) = max(r(node.left)+r(node.right), r(node.left)+s(node.right), s(node.left)+r(node.right), s(node.left)+s(node.right))
        # 直接返回两种值，跟定义两个方法相比，时间复杂度更低，相当于使用了备忘录
        nodeMap = {}
        
        def dfs(node):
            if node == None:
                return 0, 0
            if node in nodeMap:
                return nodeMap[node]

            rl, sl = dfs(node.left)
            rr, sr = dfs(node.right)
            r = node.val + sl + sr
            s = max(rl, sl) + max(rr, sr)
            return r, s

        r, s = dfs(root)
        return max(r, s)

                
# @lc code=end



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#

