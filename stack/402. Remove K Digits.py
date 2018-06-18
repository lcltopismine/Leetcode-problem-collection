    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        n = len(num)-k
        if n<=0:
            return '0'
        array = list(num)
        queue = []
        top = 0
        for ele in num:
            while top>0 and array[top-1]>ele and k>0:
                k-=1
                top-=1
            array[top] = ele
            top+=1
        for i in range(len(array)):
            if array[i]!='0':
                break
        if i==n:
            return '0'
        return "".join(array[i:n])
