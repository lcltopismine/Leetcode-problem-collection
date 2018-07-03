class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def get_max(node1,node2):
            return (node1 if node1.val > node2.val else node2) if node1 and node2 else node1 or node2

        def get_min(node1,node2):
            return (node1 if node1.val < node2.val else node2) if node1 and node2 else node1 or node2
        ##only swap when abnormal value shows
        ##must be total 2 values abnormal vary in 3 different intervals.
        self.small = self.big = None
        def dfs(root):
            if root:
                minLeft,maxLeft = dfs(root.left)
                if maxLeft and maxLeft.val > root.val:
                    self.small = root if (not self.small) or self.small.val > root.val else self.small
                    self.big = maxLeft if (not self.big) or self.big.val < maxLeft.val else self.big    
                minRight,maxRight = dfs(root.right)
                if minRight and root.val > minRight.val::
                    self.small = minRight if (not self.small) or self.small.val > minRight.val else self.small
                    self.big = root if (not self.big) or self.big.val < root.val else self.big
                return get_min(get_min(minLeft,minRight),root),get_max(get_max(maxLeft,maxRight),root)
            return None,None

        dfs(root)
        if self.small and self.big:
            self.small.val,self.big.val = self.big.val,self.small.val
