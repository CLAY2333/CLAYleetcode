
### Linked List Cycle :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/linked-list-cycle](https://leetcode-cn.com/problems/linked-list-cycle)
- 执行时间/Runtime: 48 ms 
- 内存消耗/Mem Usage: 15.7 MB
- 通过日期/Accept Datetime: 2019-12-06 09:38
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val=='liu':
                return True
            else:
                head.val='liu'
            head = head.next
        return False


```
