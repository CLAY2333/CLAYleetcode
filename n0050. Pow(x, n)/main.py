// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1.0
        now_n=abs(n)
        while(now_n):
            if now_n==0:
                break
            if(now_n%2!=0):
                res*=x
            x*=x
            now_n=now_n//2
        if n<0:
            return 1/res
        else:
            return res
