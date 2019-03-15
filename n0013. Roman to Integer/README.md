
### Roman to Integer :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/roman-to-integer](https://leetcode-cn.com/problems/roman-to-integer)
- 执行时间/Runtime: 88 ms 
- 内存消耗/Mem Usage: 10.9 MB
- 通过日期/Accept Datetime: 2019-03-01 14:47
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            sum+=value[s[i]]
        sum -= (s.count('IV') * 2)
        sum -= (s.count('IX') * 2)
        sum -= (s.count('XL') * 20)
        sum -= (s.count('XC') * 20)
        sum -= (s.count('CD') * 200)
        sum -= (s.count('CM') * 200)
        return sum

```
