
### Reverse Integer :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/reverse-integer](https://leetcode-cn.com/problems/reverse-integer)
- 执行时间/Runtime: 40 ms 
- 内存消耗/Mem Usage: 10.6 MB
- 通过日期/Accept Datetime: 2019-02-28 12:40
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def reverse(self, x):
        if(x>0):
            x=str(x)
            y = list(x)
            for i in range(len(x)):
                y[i]=x[len(x)-i-1]
            s=''.join(y)
            s=int(s)
            if(s>2147483648):
                return 0
            return s
        else:
            x=x*(-1)
            x = str(x)
            y = list(x)
            for i in range(len(x)):
                y[i]=x[len(x)-i-1]
            s = ''.join(y)
            s = int(s)
            s=s*(-1)
            if(s<-2147483648):
                return 0            
            return s


```
