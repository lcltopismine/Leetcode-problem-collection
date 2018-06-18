#import op
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #for given array:
        #compute according to the order
        #Round 1 finish "*/",find its correct input numbers,check the sign, if '*/'
        #find next number, finish computation, push back
        #round 2 finish '+-' by queue;
        #check ' ' accordingly, although not save too much time;
        self.op = []
        self.num = []
        i=0
        count = 0
        flag = 0

        while i<len(s):
            while i<len(s):
                if s[i]==" ":
                    i+=1
                    continue
                elif s[i].isdigit():
                    flag = 1
                    count*=10
                    count+=int(s[i])
                    i+=1
                else:
                    break
            if flag:
                self.num.append(count)
            count,flag = 0,0
            if i<len(s):
                if s[i] in ['+','-']:
                    self.op.append(s[i])
                elif s[i] in ['*','/']:
                    a = self.num.pop(-1)
                    count = 0
                    q = i
                    i+=1
                    while i<len(s):
                        if s[i]==" ":
                            i+=1
                            continue
                        elif s[i].isdigit():
                            count*=10
                            count+=int(s[i])
                            i+=1
                        else:
                            break
                    b = count
                    if s[q]=='*':
                        self.num.append(a*b)
                    elif s[q]=='/':
                        self.num.append(a/b) 
                    #print a,b
                    count = 0
                    i-=1
                i+=1
        #print self.op
        #print self.num
        while self.op:
            ope = self.op.pop(0)
            a,b = self.num.pop(0),self.num.pop(0)
            if ope=='+':
                self.num.insert(0,a+b)
            else:
                self.num.insert(0,a-b)
            #print self.num

        return self.num[-1]
