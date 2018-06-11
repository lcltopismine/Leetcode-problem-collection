class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ['(','{','[']
        match = {')':'(',']':'[','}':'{'}
        for ele in s:
            if ele in left:
                stack.append(ele)
            else:
                if stack and ele in match and match[ele]==stack.pop(-1):
                    pass
                else:
                    return False
        if stack:
            return False
        return True
