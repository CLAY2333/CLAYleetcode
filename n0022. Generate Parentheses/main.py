// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def loop(self,n:int,re:list,Str:str,stu:int):
        if(n>0):
            if(stu<0 or stu>n):
                return 0
            self.loop(n,re,Str+'(',stu+1)
            if(stu-1>=0):
                self.loop(n-1,re,Str+')',stu-1)
        else:
            re.append(Str)
    def generateParenthesis(self, n: int) -> list:
        re=[]
        Str=''
        stu=0
        self.loop(n,re,Str,stu)
        return re
