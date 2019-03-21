// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        D=[2, 3, 5, 7, 11, 13, 17, 19]
        sum=0
        for i in range(L,R+1):
            if str(bin(i))[2:len(bin(i))].count('1') in D:
                sum+=1
        return sum
