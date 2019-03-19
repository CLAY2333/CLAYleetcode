
### Next Greater Element I :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/next-greater-element-i](https://leetcode-cn.com/problems/next-greater-element-i)
- 执行时间/Runtime: 76 ms 
- 内存消耗/Mem Usage: 10.9 MB
- 通过日期/Accept Datetime: 2019-03-19 19:13
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp=[]
        for i in nums1:
            for j in range(nums2.index(i),len(nums2)):
                if(nums2[j]>i):
                    temp.append(nums2[j])
                    break
                else:
                    if j == len(nums2)-1:
                        temp.append(-1)
        return temp


```
