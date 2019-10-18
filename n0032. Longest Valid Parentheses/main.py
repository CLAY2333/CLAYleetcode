// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        Stack=[]
        Max=0
        Stack.append(-1)
        for index,value in enumerate(s):
            if value!=')':
                Stack.append(index)
            else:
                if Stack[-1]!=-1 and s[Stack[-1]]=='(':
                    del Stack[-1]
                    if index-Stack[-1]>Max:
                         Max=index-Stack[-1]
                else:
                    Stack.append(index)
        return Max
