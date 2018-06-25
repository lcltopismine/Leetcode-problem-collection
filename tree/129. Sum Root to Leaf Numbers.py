# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        squeue = [""]
        tol = 0
        while queue:
            cur,scur = queue.pop(0),squeue.pop(0)
            if cur:
                scur+=str(cur.val)
                if not cur.left and not cur.right:
                    tol+= int(scur)
                else:
                    if cur.left:
                        queue.append(cur.left)
                        squeue.append(scur)
                    if cur.right:
                        queue.append(cur.right)
                        squeue.append(scur)
                #print squeue
        return tol
                
