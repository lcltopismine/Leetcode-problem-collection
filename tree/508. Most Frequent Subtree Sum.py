# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = {}
        self.maxkey = []
        self.maxval = 1
        if not root:
            return []
        def rec(root):
            if not root:
                return float('-inf')
            left,right = rec(root.left),rec(root.right)
            subsum = float('-inf')
            if left==float('-inf') and right ==float('-inf'):
                subsum = root.val
            elif left==float('-inf'):
                subsum = root.val+right
            elif right==float('-inf'):
                subsum = root.val+left
            else:
                subsum = root.val+left+right
            #print left,right,root.val,subsum
            if subsum!=float('-inf'):
                if subsum not in self.res:
                    self.res[subsum] = 1
                else:
                    self.res[subsum] +=1
                if self.res[subsum]>self.maxval:
                    del self.maxkey[:]
                    self.maxkey.append(subsum)
                    self.maxval = self.res[subsum]
                elif self.res[subsum]==self.maxval:
                    self.maxkey.append(subsum)
            #print self.maxkey,self.maxval
            return subsum
        rec(root)
        #print self.res
        return self.maxkey
                
            
            
            
