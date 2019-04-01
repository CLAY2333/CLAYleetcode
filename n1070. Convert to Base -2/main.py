// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def baseNeg2(self, N: int) -> str:
        if(N==0 or N==1):
            return str(N)
        re_str=''
        while 1:
            temp_1=int(N%(-2))
            re_str+=str(abs(temp_1))
            N=(N+temp_1)//-2
            if(N==0):
                L=list(re_str)
                L.reverse()
                return ''.join(L)
