// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def numWays(self, n: int) -> int:
        c=0
        a=0
        b=1
        if n==0:
            return 1
        for i in range(n):
            c=a+b
            a=b
            b=c
        return c%1000000007
