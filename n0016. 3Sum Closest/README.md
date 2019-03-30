
### 3Sum Closest :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/3sum-closest](https://leetcode-cn.com/problems/3sum-closest)
- 执行时间/Runtime: 920 ms 
- 内存消耗/Mem Usage: 13.4 MB
- 通过日期/Accept Datetime: 2019-03-30 14:26
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def threeSumClosest(self, nums: list,target: int) -> int:
        L=len(nums)
        if(L<3):
            return 0
        nums=sorted(nums)
        min=abs(nums[0]+nums[1]+nums[2]-target)
        re=nums[0]+nums[1]+nums[2]
        for index,value in enumerate(nums):
            start=0
            end=L-1
            while(start<end):
                if(start==index):
                    start+=1
                    continue
                elif(end==index):
                    end-=1
                    continue
                if(abs(nums[start]+nums[end]+value-target)<min):
                    re=nums[start]+value+nums[end]
                    min=abs(abs(nums[start]+nums[end]+value-target))
                else:
                    if (nums[start]+nums[end]+value) < target:
                        start+=1
                    else:
                        end-=1

        return re

```
