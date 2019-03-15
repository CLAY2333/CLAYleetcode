// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new=head
        list_my=[]
        while(new!=None):
            list_my.append(new.val)
            new=new.next
        list_my=list(set(list_my))
        list_my=sorted(list_my)
        re=head
        for i in range(len(list_my)):
            head.val=list_my[i]
            if(i+1==len(list_my)):
                head.next=None
            else:
                head=head.next
        return re
