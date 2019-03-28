
### 3Sum :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/3sum](https://leetcode-cn.com/problems/3sum)
- 执行时间/Runtime: 1048 ms 
- 内存消耗/Mem Usage: 16.8 MB
- 通过日期/Accept Datetime: 2019-03-28 16:12
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def threeSum(self, nums: list) -> list:
        L=len(nums)
        if L < 3:
            return []
        nums=sorted(nums)
        if nums[L-1]<0 or nums[0]>0:
            return []
        res=[]
        for index,value in enumerate(nums):
            target=value*-1
            start=index+1
            end=L-1
            if nums[end]<0 or value>0:
                break
            if index>0  and value==nums[index-1]:
                continue
            while start<end:
                if nums[end]<0:
                    break
                if(nums[start]+nums[end]==target):
                    temp=[nums[start],value,nums[end]]
                    res.append(temp)
                    while start<end and nums[start]==nums[start+1]:
                        start+=1
                    while start<end and nums[end]==nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
                elif(nums[start]+nums[end]<target):
                    start+=1
                else:
                    end-=1
        return res


```
