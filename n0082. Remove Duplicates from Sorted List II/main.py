// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_head=ListNode(-999)
        pre_head.next=head
        now=pre_head
        while now!=None:
            if(now.next!=None and now.next.next!=None and now.next.val==now.next.next.val):
                temp_value=now.next.val
                temp_node=now.next
                while temp_node!=None :
                    if temp_node.next!=None and temp_node.next.val==temp_value :
                        temp_node=temp_node.next

                    else:
                        now.next = temp_node.next
                        break
            else:
                now=now.next
        return pre_head.next
