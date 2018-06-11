class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        stacks,stackt = [],[]
        for ele in S:
            if ele!='#':
                stacks.append(ele)
            else:
                if stacks:
                    stacks.pop(-1)
        for ele in T:
            if ele!='#':
                stackt.append(ele)
            else:
                if stackt:
                    stackt.pop(-1)
        s = "".join(stacks)
        t = "".join(stackt)
        if s==t:
            return True
        return False
