# 给出一个元素无序数组，找出符合条件的数，使得其左边的数都小于它，右边的数都大于它
# 要求：时间复杂度O(n)

# 思路：单调递增栈（底->顶）
# 1. 遍历所有元素，放入单调递增栈
# 2. 一旦发现更小的元素，就将栈顶元素出栈直到栈顶元素更小，再考虑新元素入栈
# 3. 为了确保新元素入栈时是栈中出现过的最大的数，需要有一个值存储最大值

def findMidNum(nums):
    maxN = 0
    stack = []
    for i in nums:
        while stack and stack[-1] > i:
            stack.pop()
        if i > maxN:
            stack.append(i)
            maxN = i
    return stack

arr = [2,3,1,8,9,20,12]
print(findMidNum(arr))
