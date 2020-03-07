// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def fib(self, n: int) -> int:
        s={}
        def loop(n):
            if n==0:
                return 0
            elif n==1:
                return 1
            elif n==2:
                return 1
            elif n==3:
                return 2
            else:
                if (n-1) not in s:
                    s[n-1]=loop(n-1)
                    temp1=s[n-1]
                else:
                    temp1=s[n-1]
                if (n-2) not in s:
                    s[n-2]=loop(n-2)
                    temp2=s[n-2]
                else:
                    temp2 = s[n - 2]
                return temp1+temp2
        return loop(n)%1000000007
