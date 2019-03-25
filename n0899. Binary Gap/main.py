// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        N_2=str(bin(N))
        temp=0
        temp_1=0
        temp_2=0
        max=0
        for i in range(len(N_2)):
            if N_2[i]=='1':
                if temp_1==0:
                    temp_1=i
                    temp_2=i
                else:
                    temp_1=temp_2
                    temp_2=i
            if (temp_2-temp_1) > max:
                max=temp_2-temp_1
        return max
