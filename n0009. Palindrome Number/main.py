// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x>=0):
            if(x==0):
                 return True
            x=str(x)
            y = list(x)
            for i in range(len(x)):
                y[i]=x[len(x)-i-1]
            s=''.join(y)
            s=int(s)
            if(s==int(x)):
                return True
            else:
                return False
        else:
           return False