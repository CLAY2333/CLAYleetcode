// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_2=str(bin(num))
        re=''
        for i in num_2[2:len(num_2)]:
            if(i=='1'):
                re+='0'
            else:
                re+='1'
        result=int(re,2)
        return result
