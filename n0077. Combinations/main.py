// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def combine(self, n: int, k: int) -> list:
        L=[]
        for i in range(1,n+1):
            L.append(i)
        re=[]
        times=0
        while(times<pow(2,len(L))):
            S=str(bin(times))
            S=S[2::]
            if S.count('1')==k:
                temp=[]
                for index,value in enumerate(S):
                    if value=='1':
                        temp.append(L[len(S)-index-1])
                re.append(temp.copy())
            times+=1
        return re
