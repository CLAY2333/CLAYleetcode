// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        Sum=sum(A)
        if(len(A)<3):
            return False
        if(Sum%3!=0):
            return False
        SS=0
        aver=int(Sum/3)
        for x in range(len(A)):
            SS+=A[x]
            if(SS==aver):
                SS=0
        if(SS==0):
            return True
        return False
