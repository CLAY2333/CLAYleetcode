
### Jewels and Stones :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/jewels-and-stones](https://leetcode-cn.com/problems/jewels-and-stones)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-04-29 16:06
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        nums=0
        for i in S:
            if i in J:
                nums+=1
        return nums

```
