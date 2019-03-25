
### Median of Two Sorted Arrays :star::star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/median-of-two-sorted-arrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays)
- 执行时间/Runtime: 356 ms 
- 内存消耗/Mem Usage: 11.9 MB
- 通过日期/Accept Datetime: 2019-03-25 01:47
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        temp=nums1+nums2
        temp=sorted(temp)
        L=len(temp)
        if(L%2==0 or L==2):
            return (temp[int(L/2)]+temp[int(L/2)-1])*0.5
        else:
            return (temp[int(L/2)])

```
