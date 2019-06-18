
### Search in Rotated Sorted Array II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii)
- 执行时间/Runtime: 52 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-06-18 17:05
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def search(self, nums: list, target: int) -> int:
        if(len(nums)==0):
            return False
        left=0
        right=len(nums)-1
        while(1):
            mid = (left + right) // 2
            if(target==nums[left]):
                return True
            if (target == nums[right]):
                return True
            if (target == nums[mid]):
                return True
            if left==right or abs(left-right)==1:
                return False
            if(nums[left]==nums[mid]==nums[right]):
                left+=1
                right-=1
                continue
            if(nums[left]==nums[mid]):
                left=mid+1
                continue
            if(nums[mid]==nums[right]):
                right=mid-1
                continue
            if(nums[left]<nums[mid]):
                if(target>=nums[left] and target<nums[mid]):
                    left+=1
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(target<=nums[right] and target>nums[mid]):
                    left=mid+1
                    right-=1
                else:
                    right=mid-1

```
