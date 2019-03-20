
### Sort Array By Parity II :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/sort-array-by-parity-ii](https://leetcode-cn.com/problems/sort-array-by-parity-ii)
- 执行时间/Runtime: 168 ms 
- 内存消耗/Mem Usage: 12.9 MB
- 通过日期/Accept Datetime: 2019-03-20 00:35
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index_1=1
        index_2=0
        temp=[0]*len(A)
        for i in A:
            if i%2==0:
                temp[index_2]=i
                index_2+=2
            else:
                temp[index_1]=i
                index_1+=2
        return temp

```
