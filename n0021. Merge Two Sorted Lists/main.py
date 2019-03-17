// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=list()
        num2=list()
        i=0
        if(l1==None and l2==None):
            return l1
        if (l1 == None ):
            return l2
        if ( l2 == None):
            return l1
        link=l1
        while(1):
            num1.append(link.val)
            link=link.next
            if(link==None):
                break
            i+=1
        link=l2
        i=0
        while(1):
            num2.append(link.val)
            link=link.next
            if(link==None):
                break
            i+=1
        num1.extend(num2)
        num1.sort()
        result=ListNode(num1[0])
        i=1
        link1 = ListNode(None)
        result.next=link1
        for i in range(1,len(num1)):
            link1.val=num1[i]
            link2=ListNode(None)
            if(i==len(num1)-1):
                break  
            link1.next=link2
            link1=link2
        return result
