// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value=[]
        return None

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.value.insert(0,x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if(len(self.value)==0):
            return False
        return self.value.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if(len(self.value)==0):
            return False
        return self.value[len(self.value)-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if(len(self.value)==0):
            return True
        else:
            return False
