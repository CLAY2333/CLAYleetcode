
### Find First and Last Position of Element in Sorted Array :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array)
- 执行时间/Runtime: 56 ms 
- 内存消耗/Mem Usage: 13.9 MB
- 通过日期/Accept Datetime: 2019-04-05 14:32
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left=0
        right=len(nums)-1
        if(len(nums)==0 or target<nums[left] or target>nums[right] ):
            return [-1,-1]
        while(left<=right):
            mid=(left+right)//2
            if(target==nums[mid]):
                temp_left=mid
                temp_right=mid
                while(temp_left>=0 and nums[temp_left]==target ):
                    temp_left-=1
                while( temp_right<len(nums) and nums[temp_right]==target):
                    temp_right+=1
                return [temp_left+1,temp_right-1]
            if(target<nums[mid]):
                right=mid-1
            elif(target>nums[mid]):
                left=mid+1
        return [-1,-1]

```
