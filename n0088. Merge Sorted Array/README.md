
### Merge Sorted Array :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/merge-sorted-array](https://leetcode-cn.com/problems/merge-sorted-array)
- 执行时间/Runtime: 44 ms 
- 内存消耗/Mem Usage: 10.7 MB
- 通过日期/Accept Datetime: 2019-03-15 15:33
```python
// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop()
        for i in range(n):
            nums1.append(nums2[i])
        nums1.sort()

```
