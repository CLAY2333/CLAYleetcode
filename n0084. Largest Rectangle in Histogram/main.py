// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def largestRectangleArea(self, heights: list) -> int:
        def push(Stack:list,ele:int):
            Stack.append(ele)

        def pop(Stack:list):
            ele=Stack[-1]
            del Stack[-1]
            return ele
        def top(Stack):
            return Stack[-1]

        Stack=[]
        push(Stack,-1)
        maxArea=0
        for index,value in enumerate(heights):
            if index>0 and heights[top(Stack)]>=value:
                while 1:
                    Area=heights[top(Stack)]*(index-Stack[len(Stack)-2]-1)
                    if Area>maxArea:
                        maxArea=Area
                    pop(Stack)
                    if(top(Stack)==-1):
                        break
                    if not (index > 0 and heights[top(Stack)] > value):
                        break
            push(Stack,index)
            PP=[]
            PP.append(Stack[-1])
        while Stack[-1]!=-1 :
            Area=heights[Stack[-1]]*(PP[0]-Stack[len(Stack)-2])
            if Area>maxArea:
                maxArea=Area
            pop(Stack)
        return maxArea
