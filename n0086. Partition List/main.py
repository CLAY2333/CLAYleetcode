// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head==None:
            return []
        node_list=[]
        while head!=None:
            node_list.append(head.val)
            head=head.next
        one=[]
        two=[]
        for i in node_list:
            if i >=x:
                two.append(i)
            else:
                one.append(i)
        node_list=one+two
        head=ListNode(node_list[0])
        node_list.pop(0)
        temp=head
        for i in node_list:
            N=ListNode(i)
            temp.next=N
            temp=temp.next
        return head
