// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def countSegments(self, s: str) -> int:
        if(len(s)==0):
            return 0
        L=s.split(' ')
        nums=0
        for index,value in enumerate(L):
            if(len(value)!=0):
                nums+=1
        return nums
