# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def rec(root,p=None):
            if root:
                root.p = p
                rec(root.left,root)
                rec(root.right,root)
        rec(root)
        queue=[(target,0)]
        checked = {target}
        while queue:
            if queue[0][1]==K:
                return [node.val for node,d in queue]
            node,d = queue.pop(0)
            for ele in [node.left,node.right,node.p]:
                if ele and ele not in checked:
                    checked.add(ele)
                    queue.append((ele,d+1))
        return []
            
            
