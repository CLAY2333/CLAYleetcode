
### Fizz Buzz :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/fizz-buzz](https://leetcode-cn.com/problems/fizz-buzz)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 14.8 MB
- 通过日期/Accept Datetime: 2019-11-22 20:16
```python
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

```
