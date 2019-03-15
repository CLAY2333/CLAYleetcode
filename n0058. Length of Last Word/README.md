
### Length of Last Word :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/length-of-last-word](https://leetcode-cn.com/problems/length-of-last-word)
- 执行时间/Runtime: 16 ms 
- 内存消耗/Mem Usage: 11 MB
- 通过日期/Accept Datetime: 2019-03-13 21:16
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        lens=len(s)
        num=s.rfind(" ")
        if(num==-1):
            return lens
        sum=lens-num
        return sum-1

```
