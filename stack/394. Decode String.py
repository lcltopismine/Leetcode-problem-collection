class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.nums = []
        self.chars = []
        i = 0
        while i<len(s):
            cur = 0
            while s[i]>='0' and s[i]<='9':
                cur*=10
                cur+=int(s[i])
                i+=1
            if cur:
                self.nums.append(cur)
            if s[i]!=']':
                self.chars.append(s[i])
            else:
                tepstr = ''
                while self.chars[-1]!='[':
                    tepstr=self.chars.pop(-1)+tepstr
                self.chars.pop(-1)
                curnum = self.nums.pop(-1)
                self.chars.append(tepstr*curnum)
            i+=1
        return "".join(self.chars)
