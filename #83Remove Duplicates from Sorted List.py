# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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
        print(list_my)
        re=head
        for i in range(len(list_my)):
            head.val=list_my[i]
            if(i+1==len(list_my)):
                head.next=None
            else:
                head=head.next
        return re

if __name__=='__main__':
    s=Solution()
    l1=ListNode(-1)
    l1_2=ListNode(0)
    l1_4=ListNode(0)
    l1_5 = ListNode(3)

    l1.next=l1_2
    l1_2.next=l1_4
    l1_4.next=l1_5
    f=s.deleteDuplicates(l1)
    print(f.val)
    #f=f.next
    #print(f.val)
    #f=f.next
    #print(f.val)
