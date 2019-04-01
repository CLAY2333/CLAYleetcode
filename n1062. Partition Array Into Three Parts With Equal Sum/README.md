
### Partition Array Into Three Parts With Equal Sum :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum)
- 执行时间/Runtime: 1236 ms 
- 内存消耗/Mem Usage: 17.4 MB
- 通过日期/Accept Datetime: 2019-03-24 11:18
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        Sum=sum(A)
        if(len(A)<3):
            return False
        if(Sum%3!=0):
            return False
        SS=0
        aver=int(Sum/3)
        for x in range(len(A)):
            SS+=A[x]
            if(SS==aver):
                SS=0
        if(SS==0):
            return True
        return False

```
