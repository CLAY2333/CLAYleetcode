// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head==None:
            return False
        quick_head = head.next
        slow_head = head
        while quick_head!=slow_head:
            if quick_head == None or quick_head.next is None:
                return False
            quick_head = quick_head.next.next
            slow_head = slow_head.next
        return True
