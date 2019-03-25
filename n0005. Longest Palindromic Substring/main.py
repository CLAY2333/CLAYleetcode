// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(list(set(list(s))))==1:
            return s
        max_len=0
        i=0
        j=0
        Len=len(s)
        dp=[[0] * Len for w in range(Len)]
        for x in range(Len):
            for y in range(x):
                dp[y][x]=(s[x]==s[y])&(dp[y+1][x-1]|(x-y<2))
                if(dp[y][x] and max_len<x-y+1):
                    i=y
                    j=x
                    max_len=x-y+1
            dp[x][x]=1
        return s[i:j+1]
