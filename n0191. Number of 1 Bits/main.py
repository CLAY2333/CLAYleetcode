// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num=0
        n=bin(n)
        for i in n:
            if i=='1':
                num+=1
        return num
