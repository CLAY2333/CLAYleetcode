
### Remove Duplicates from Sorted Array II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii)
- 执行时间/Runtime: 68 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-05-13 14:54
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        delete_list=[]
        for index,value in enumerate(nums):
            if index>1 and value==nums[index-2]:
                delete_list.insert(0,index)
        for i in delete_list:
            nums.pop(i)
        return len(nums)

```
