# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        h = height(root)
        subgrid = ["" for i in range(2**h-1)]
        grid = [subgrid[:] for i in range(h)]
        def rec(root,level,left,right,grid):
            if not root:
                return
            if root:
                grid[level-1][(left+right)//2] += str(root.val)
                rec(root.left,level+1,left,(left+right)/2-1,grid)
                rec(root.right,level+1,(left+right)/2+1,right,grid)
        rec(root,1,0,len(grid[0])-1,grid)
        return grid
