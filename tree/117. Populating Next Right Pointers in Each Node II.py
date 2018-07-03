# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            queue = [[root,1]]
            while queue:
                cur,level = queue.pop(0)
                if level>1:
                    if level==olevel:
                        pre.next = cur
                if cur.left:
                    queue.append([cur.left,level+1])
                if cur.right:
                    queue.append([cur.right,level+1])
                pre,olevel = cur,level
        
