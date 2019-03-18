// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        temp=math.log10(n)/math.log10(3)
        temp=temp%1
        if(temp==0):
            return True
        else:
            return False
