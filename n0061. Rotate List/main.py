// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if(k==0):
            return head
        if head==None:
            return head
        link1=head
        link2=ListNode(-999)
        link2.next=head
        times=0
        while(link1.next):
            link1=link1.next
            times+=1
            if(times>=k):
                link2=link2.next
        times+=1

        if(times<=k):
            k=k%(times)
            if(k==0):
                return head
        link1=head
        link2=ListNode(-999)
        link2.next=head
        times=0
        while(link1.next):
            link1=link1.next
            times+=1
            if(times>=k):
                link2=link2.next
        temp=link2.next
        link2.next=None
        link1.next=head
        return temp
