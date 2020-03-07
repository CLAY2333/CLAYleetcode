
### Linked List Cycle II :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/linked-list-cycle-ii](https://leetcode-cn.com/problems/linked-list-cycle-ii)
- 执行时间/Runtime: 60 ms 
- 内存消耗/Mem Usage: 16 MB
- 通过日期/Accept Datetime: 2019-12-06 22:55
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head==None:
            return head
        quick_head=head.next
        slow_head=head
        while quick_head!=slow_head:
            if quick_head==None or quick_head.next==None:
                return None
            quick_head=quick_head.next.next
            slow_head=slow_head.next
        piont_head=head
        while slow_head.next!=piont_head:
            piont_head=piont_head.next
            slow_head=slow_head.next
        return piont_head

```
