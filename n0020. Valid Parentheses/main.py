// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Stack:
    """模拟栈"""

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs=Stack()
        for i in range(len(s)):
            strs.push(s[i])
        strs_Valid=Stack()
        for i in range(len(s)):
            if(strs_Valid.isEmpty()):
                strs_Valid.push(strs.pop())
            else:
                if(strs_Valid.peek()==']' and strs.peek()=='['):
                    strs.pop()
                    strs_Valid.pop()
                else:
                    if (strs_Valid.peek() == ')' and strs.peek() == '('):
                        strs.pop()
                        strs_Valid.pop()
                    else:
                        if (strs_Valid.peek() == '}' and strs.peek() == '{'):
                            strs.pop()
                            strs_Valid.pop()
                        else:
                            strs_Valid.push(strs.pop())
        if(strs_Valid.isEmpty()):
            return True
        else:
            return False
