# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.nums = {}
        self.maxnum = 0
        self.mnum = []
        def rec(root):
            if not root:
                return
            if root:
                rec(root.left)
                if root.val not in self.nums:
                    self.nums[root.val] = 1
                else:
                    self.nums[root.val] += 1
                if self.nums[root.val] ==self.maxnum:
                    self.mnum.append(root.val)
                elif self.nums[root.val] >self.maxnum:
                    del self.mnum[:]
                    self.mnum.append(root.val)
                    self.maxnum = self.nums[root.val]
                rec(root.right)
        rec(root)
        return self.mnum
            
