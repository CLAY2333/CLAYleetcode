// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None:
            return head
        temp=head
        first=0
        second=0
        times=0
        while temp!=None:
            temp=temp.next
            times+=1
            if times==(k):
                head=self.reverseBetween(head,first+1,second+1)
                first=second+1
                times=0
            second += 1
        return head

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if (head.next == None or m == n):
            return head
        first_node = head
        second_node = head
        qiang = ListNode(-9)
        qiang.next = head
        head = qiang
        n += 1
        m += 1
        temp = ListNode(-999)
        temp.next = head
        num = 0
        while temp != None:
            if num == n - 1:
                second_node = temp
                break
            else:
                if (num == m - 1):
                    first_node = temp
                num += 1
                temp = temp.next
        head_short = first_node.next
        w_short = second_node.next
        d = w_short.next
        head_short_while = head_short
        next_head = head_short_while.next
        next_next_head = next_head.next
        time = 0
        while (time != n - m and next_next_head != None):
            next_head.next = head_short_while
            head_short_while = next_head
            next_head = next_next_head
            next_next_head = next_head.next
            time += 1
        if (time != n - m):
            next_head.next = head_short_while
            if (first_node.val == -9):
                head_short.next = None
                return next_head
            first_node.next = next_head
            head_short.next = None
            return head.next
        first_node.next = w_short
        head_short.next = d
        return head.next
