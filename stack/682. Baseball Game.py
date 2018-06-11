class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        self.sum = 0
        stack = []
        for ele in ops:
            if ele[0] not in ['+','D','C']:
                stack.append(int(ele))
                self.sum+= int(ele)
            elif ele =='D':
                self.sum += stack[-1]*2
                stack.append(stack[-1]*2)
            elif ele=='C':
                self.sum -= stack.pop(-1)
            else:
                a = stack[-1]
                b = stack[-2]
                self.sum+=a+b
                stack.append(a+b)
        return self.sum
        
