
### Implement strStr() :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/implement-strstr](https://leetcode-cn.com/problems/implement-strstr)
- 执行时间/Runtime: 16 ms 
- 内存消耗/Mem Usage: 11 MB
- 通过日期/Accept Datetime: 2019-03-05 11:38
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def strStr(self, haystack, needle):
        if(needle==None):
            return 0
        return haystack.find(needle)

```
