
### Number of Segments in a String :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/number-of-segments-in-a-string](https://leetcode-cn.com/problems/number-of-segments-in-a-string)
- 执行时间/Runtime: 76 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-05-22 15:22
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def countSegments(self, s: str) -> int:
        if(len(s)==0):
            return 0
        L=s.split(' ')
        nums=0
        for index,value in enumerate(L):
            if(len(value)!=0):
                nums+=1
        return nums

```
