class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s="".join(s.split(" "))
        ops = []
        nums = []
        i = 0
        while i<len(s):
            count = -3
            flag = 0
            while i<len(s) and '0'<=s[i]<='9':
                flag = 1
                count = max(count,0)
                count*=10
                count+=int(s[i])
                i+=1
            if count!=-3:
                nums.append(count)
            if i<len(s):
                if s[i] in ['+','-','(']:
                    ops.append(s[i])
                elif s[i]==')':
                    newop = []
                    newnum = []
                    while ops[-1]!='(':
                        newnum.append(nums.pop(-1))
                        newop.append(ops.pop(-1))
                    ops.pop(-1)
                    newnum.append(nums.pop(-1))
                    #print ops,nums
                    #print newop,newnum
                    while newop:
                        #print newop
                        op = newop.pop(-1)
                        a,b = newnum.pop(-1),newnum.pop(-1)
                        #print a,b
                        if op=='+':
                            newnum.append(a+b)
                        else:
                            newnum.append(a-b)
                    nums.append(newnum.pop(-1))
            #print nums
            i+=1
        #print ops
        #print nums
        while ops:
            op = ops.pop(0)
            a,b = nums.pop(0),nums.pop(0)
            if op=='+':
                nums.insert(0,a+b)
            elif op=='-':
                nums.insert(0,a-b)
        #print nums
        return nums[-1]

            
                        
                    
            
        
