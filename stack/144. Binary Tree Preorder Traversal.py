    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            cur = stack.pop(-1)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            ret.append(cur.val)
        return ret
