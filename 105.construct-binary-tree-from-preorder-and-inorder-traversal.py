#
# @lc app=leetcode.cn id=105 lang=python3
# @lcpr version=30203
#
# [105] 从前序与中序遍历序列构造二叉树
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 空数组直接返回
        if len(preorder) == 0:
            return None
        # 叶子节点则直接返回
        if len(preorder) == 1:
            return TreeNode(preorder[0])


        # 使用map存储inorder中的各个值下标（因为无重复元素，节省时间复杂度）
        inorder_map = {}
        for i in range(0, len(inorder)):
            inorder_map[inorder[i]] = i

        # 从前序遍历数组中获取根节点值
        root_value = preorder[0]
        node = TreeNode(root_value)

        # 通过根节点找出中序左子树和右子树数组
        idx = inorder_map[root_value]
        left_inorder = inorder[0: idx]
        right_inorder = inorder[idx+1:]

        # 根据中序左右子树的长度找出前序左右子树数组（注意第一个元素是根节点）
        left_preorder = preorder[1: len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        # 递归构建出左右子树
        left_tree = self.buildTree(left_preorder, left_inorder)
        right_tree = self.buildTree(right_preorder, right_inorder)
        node.left = left_tree
        node.right = right_tree

        return node

# @lc code=end



#
# @lcpr case=start
# [3,9,20,15,7]\n[9,3,15,20,7]\n
# @lcpr case=end

# @lcpr case=start
# [-1]\n[-1]\n
# @lcpr case=end

#

