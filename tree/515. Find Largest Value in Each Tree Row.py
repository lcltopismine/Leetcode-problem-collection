# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = [(root,1)]
        ret = []
        curmax,curlevel = float('-inf'),1
        while queue:
            cur,level = queue.pop(0)
            if cur:
                if level!=curlevel:
                    ret.append(curmax)
                    curmax = float('-inf')
                curmax,curlevel=max(cur.val,curmax),level
                queue.append([cur.left,level+1])
                queue.append([cur.right,level+1])
            else:
                continue
        if curmax!=float('-inf'):
            ret.append(curmax)
        return ret
                
            
