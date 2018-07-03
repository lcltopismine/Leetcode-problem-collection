# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        dic,ret = {},[]
        def rec(root,dic,ret):
            if not root:
                return '#'
            left,right = rec(root.left,dic,ret),rec(root.right,dic,ret)
            tep = str(root.val)+left+right
            if tep not in dic:
                dic[tep] = 1
            else:
                if dic[tep]==1:
                    ret.append(root)
                dic[tep]+=1
            return tep
        rec(root,dic,ret)
        return ret
