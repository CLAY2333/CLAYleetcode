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

