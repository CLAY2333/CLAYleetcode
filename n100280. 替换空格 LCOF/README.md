
### 替换空格 LCOF :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2020-02-16 14:03
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def replaceSpace(self, s: str) -> str:
        res=''
        for i in s:
            if i==' ':
                res+='%20'
            else:
                res+=i
        return res

```
