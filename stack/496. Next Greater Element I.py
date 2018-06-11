class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        a,b,ret,cur = findNums,nums,[],0
        for i in range(len(a)):
            cur = a[i]
            tep = []
            for j in range(len(b)-1,-1,-1):
                if b[j]>cur:
                    tep.append(b[j])
                elif b[j]==cur:
                    if not tep:
                        ret.append(-1)
                    else:
                        #print tep
                        ret.append(tep[-1])
                    break
        return ret
