// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
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
