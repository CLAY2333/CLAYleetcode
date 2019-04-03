
### Next Permutation :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/next-permutation](https://leetcode-cn.com/problems/next-permutation)
- 执行时间/Runtime: 64 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-04-03 18:57
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        temp=nums.copy()
        ex_index=0
        for index,value in enumerate(nums):
            if(index+1<len(nums) and value>nums[index+1]):
                tem_value=value
                ex_index = index + 1
                for temp_index,x in enumerate(nums[0:index]):
                    if(x>nums[index+1] and x<tem_value):
                        tem_value=x
                        index=temp_index
                nums[index]= nums[ex_index]
                nums[ex_index]=tem_value
                break
        if(temp==nums):
            return None
        nums.reverse()
        ex_index=len(nums)-ex_index
        nums[ex_index:]=sorted(nums[ex_index:])
        return None

```
