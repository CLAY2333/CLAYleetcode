
### Jump Game II :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/jump-game-ii](https://leetcode-cn.com/problems/jump-game-ii)
- 执行时间/Runtime: 92 ms 
- 内存消耗/Mem Usage: 15.4 MB
- 通过日期/Accept Datetime: 2019-07-16 18:56
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def jump(self, nums: list) -> int:
        now=0
        times=0
        while now <len(nums)-1:
            times+=1
            temp=[]
            d={}
            for i in range(1,nums[now]+1):
                if now+i ==len(nums)-1:
                    return times
                temp.append(nums[now+i]+now+i)
                d[nums[now+i]+now+i]=now+i
            next=max(temp)
            now=d[next]
        return times

```
