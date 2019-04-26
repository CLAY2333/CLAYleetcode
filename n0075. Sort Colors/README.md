
### Sort Colors :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/sort-colors](https://leetcode-cn.com/problems/sort-colors)
- 执行时间/Runtime: 64 ms 
- 内存消耗/Mem Usage: 13 MB
- 通过日期/Accept Datetime: 2019-04-26 11:14
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        times=0
        while(times<len(nums)):
            index+=1
            if nums[index]==0:
                nums.pop(index)
                nums.insert(0,0)
            elif nums[index]==2:
                nums.pop(index)
                index-=1
                nums.append(2)
            times+=1

```
