#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 方法一：保留所有序列的动态规划，缺点是内存超出限制
        #seqs = []
        #for n in nums:
        #    find_seq = False
        #    for seq in seqs:
        #        if n > seq[-1]:
        #            new_seq = seq[:]
        #            new_seq.append(n)
        #            seqs.append(new_seq)
        #            find_seq = True
        #    if not find_seq:
        #        seqs.append([n])
        #res = 0
        #for seq in seqs:
        #    res = max(res, len(seq))
        #print(seqs)
        #return res

        # 方法二：仅保留长度信息的动态规划，复杂度 O(n^2)
        l = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    l[i] = max(l[i], l[j]+1)
        print(l)
        res = 0
        for n in l:
            res = max(res, n)
        return res

            


# @lc code=end

