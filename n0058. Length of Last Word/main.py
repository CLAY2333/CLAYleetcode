// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.rstrip()
        lens=len(s)
        num=s.rfind(" ")
        if(num==-1):
            return lens
        sum=lens-num
        return sum-1
