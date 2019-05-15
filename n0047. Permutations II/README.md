
### Permutations II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/permutations-ii](https://leetcode-cn.com/problems/permutations-ii)
- 执行时间/Runtime: 2780 ms 
- 内存消耗/Mem Usage: 13.2 MB
- 通过日期/Accept Datetime: 2019-05-15 15:18
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Loop(self,nums,now_re:list,re:list):
        for index,value in enumerate(nums):
            now_re.append(value)
            nums.pop(index)
            if(len(nums)==0):
                if not now_re in re:
                    re.append(now_re.copy())
                now_re.pop(-1)
                nums.insert(index, value)
                break
            self.Loop(nums,now_re,re)
            now_re.pop(-1)
            nums.insert(index,value)
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        re=[]
        now_re=[]
        self.Loop(nums,now_re,re)
        return re

```
