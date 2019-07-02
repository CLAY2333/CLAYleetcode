// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        hashmap={}
        if(len(s)==0 or len(words)==0):
            return []
        for i in words:
            if not i in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        n=len(words[0])
        le=len(words)

        now_hashmap={}
        tt=0
        res=[]
        for i in range(n+1):
            tt=0
            now_hashmap={}
            for times in range(len(s[i:])//n):
                if(s[i+times*n:i+times*n+n] in hashmap) and s[i+times*n:i+times*n+n] in now_hashmap:
                    now_hashmap[s[i+times*n:i+times*n+n]]+=1
                    if now_hashmap[s[i+times*n:i+times*n+n]]>hashmap[s[i+times*n:i+times*n+n]] and i+times*n+n<len(s):
                        now_hashmap[s[i+(times-tt)*n:i+(times-tt)*n+n]]-=1
                        tt-=1
                elif(s[i+times*n:i+times*n+n] in hashmap) and not s[i+times*n:i+times*n+n] in now_hashmap:
                    now_hashmap[s[i+times*n:i+times*n+n]] =1
                else:
                    tt=0
                    now_hashmap={}
                    continue
                tt+=1
                if(tt==le):
                    type=0
                    for nn in hashmap:
                        if(nn in now_hashmap) and hashmap[nn]!=now_hashmap[nn]:
                            type=1
                            break
                    if type!=1:
                        if not (i+(times+1-le)*n) in res:
                            res.append(i+(times+1-le)*n)
                        now_hashmap[s[i + (times - tt+1) * n:i + (times - tt+1) * n + n]] -= 1
                        tt-=1
                    else:
                        now_hashmap[s[i + (times - tt+1) * n:i + (times - tt+1) * n + n]] -= 1
                        tt -= 1
        return res
