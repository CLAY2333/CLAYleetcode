
### Palindrome Number :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/palindrome-number](https://leetcode-cn.com/problems/palindrome-number)
- 执行时间/Runtime: 272 ms 
- 内存消耗/Mem Usage: 13.5 MB
- 通过日期/Accept Datetime: 2019-02-27 21:48
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
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

```
