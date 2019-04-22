
### Jump Game :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/jump-game](https://leetcode-cn.com/problems/jump-game)
- 执行时间/Runtime: 1428 ms 
- 内存消耗/Mem Usage: 14.5 MB
- 通过日期/Accept Datetime: 2019-04-21 12:37
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def canJump(self, nums: list) -> bool:
        if(len(nums)<=1):
            return True
        nums.reverse()
        temp_nums=nums.copy()
        su=0
        while(1):
            for index,value in enumerate(nums):
                if(index==0):
                    continue
                if(value>=index):
                    L=len(nums)
                    su=1
                    nums=nums[index:len(nums)]
                    break
            if su==0:
                if index==len(nums)-1:
                    break
            else:
                su=0
                if(index==L):
                    break
        if(len(nums)<=1):
            return True
        else:
            return False

```
