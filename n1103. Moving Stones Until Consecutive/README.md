
### Moving Stones Until Consecutive :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/moving-stones-until-consecutive](https://leetcode-cn.com/problems/moving-stones-until-consecutive)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 12.9 MB
- 通过日期/Accept Datetime: 2019-04-28 12:02
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> list:
        min_times=0
        max_timss=0
        temp=[a,b,c]
        temp.sort()
        a=temp[0]
        b=temp[1]
        c=temp[2]
        if(b-a>1):
            min_times+=1
            max_timss+=(b-a-1)
        if(c-b>1):
            min_times+=1
            max_timss+=(c-b-1)
        if(0<b-a-1<min_times):
            min_times=b-a-1
        if(0<c-b-1<min_times):
            min_times=c-b-1
        return [min_times,max_timss]

```
