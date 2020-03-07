
### 数组中重复的数字 LCOF :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)
- 执行时间/Runtime: 424 ms 
- 内存消耗/Mem Usage: 25.9 MB
- 通过日期/Accept Datetime: 2020-02-14 13:22
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from typing import List
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        H={}
        for i in nums:
            if i in H:
                return i
            H[i]=1
        return -1

```
