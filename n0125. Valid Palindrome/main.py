// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def isPalindrome(self, s: str) -> bool:
        re=[]
        for i in s:
            if(i.isalpha() or i.isdigit()):
                re.append(i.lower())
        temp=re.copy()
        temp.reverse()
        if(temp==re):
            return True
        else:
            return False
