// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def __init__(self):
        self.times=0
        self.temp=[]
        self.res=[]
    def tostr(self,temp:list):
        S=''
        for i in temp:
            S+=i
            S+='.'
        S=S[:-1]
        return S
    def Loop(self,s):
        if len(s)==0:
            if self.times==4:
                v=self.tostr(self.temp)
                if not v in self.res:
                    self.res.append(v)
            return
        if self.times>=4:
            return 0
        self.times+=1
        for i in range(3):
            if (s[0]!='0' and int(s[:i+1])<=255) or (len(s[:i+1])==1 and int(s[:i+1])==0):
                self.temp.append(s[:i+1])
                self.Loop(s[i+1:])
                del self.temp[-1]
        self.times -= 1
        return self.res
    def restoreIpAddresses(self, s: str) -> list:
        L=len(s)
        if(L>12):
            return []
        else:
            return self.Loop(s)
