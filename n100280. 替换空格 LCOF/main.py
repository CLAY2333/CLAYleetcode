// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def replaceSpace(self, s: str) -> str:
        res=''
        for i in s:
            if i==' ':
                res+='%20'
            else:
                res+=i
        return res
