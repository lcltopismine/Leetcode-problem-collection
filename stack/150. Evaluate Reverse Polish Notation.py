#pay attention to cut off loss in '/'
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        numstack = []
        ops = ['+','-','*','/']
        for ele in tokens:
            if ele not in ops:
                numstack.append(int(ele))
            else:
                n1,n2 = numstack.pop(-1),numstack.pop(-1)
                if ele=='+':
                    numstack.append(n2+n1)
                elif ele=='-':
                    numstack.append(n2-n1)
                elif ele=='*':
                    numstack.append(n2*n1)
                elif ele=='/':
                    if n1*n2>0:
                        numstack.append(int(1.0*abs(n2)/abs(n1)))
                    else:
                        numstack.append(int(-1.0*abs(n2)/abs(n1)))
        #print numstack
        return int(numstack[-1])

#@vajpeyi his code is also good.
import operator as op
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops={'+':op.add,"-":op.sub,"*":op.mul,'/': (lambda x,y:int(float(x)/y))}
        stack=[]
        l=['+','-','*','/']
        for i in tokens:
            if i not in l:
                stack.append(i)
            else:
                j=int(stack.pop())
                k=int(stack.pop())
                n=ops[i](k,j)
                #print(n)
                stack.append(n)
        return int(stack[0]  )  
