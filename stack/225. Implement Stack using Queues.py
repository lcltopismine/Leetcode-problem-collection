class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.num = 0
        self.topele =-1
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        self.topele = x
        self.num+=1
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        tep = []
        res = -1
        cur = self.num
        cache = 0
        while self.queue and cur>1:
            cache = self.queue.pop(0)
            tep.append(cache)
            cur-=1
        res = self.queue.pop(0)
        self.topele = cache
        #print tep,res
        self.num-=1
        while tep:
            self.queue.append(tep.pop(0))
        return res
            

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.topele

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.num==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
