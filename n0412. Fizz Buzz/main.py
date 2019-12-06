// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def fizzBuzz(self, n: int) -> list:
        def is3(n):
            s=str(n)
            sum=0
            for i in s:
                sum+=int(i)
            if sum%3==0:
                return True
            else:
                return False
        def is5(n):
            s=str(n)
            if(s[-1]=='0' or s[-1]=='5'):
                return True
            else:
                return False
        ss=''
        st=0
        res=[]
        for i in range(1,n+1):
            if is3(i):
                ss+='Fizz'
                st=1
            if is5(i):
                ss+='Buzz'
                st=1
            if st==1:
                res.append(ss)
                st=0
                ss=''
            else:
                res.append(str(i))
                st=0
                ss=''
        return res
