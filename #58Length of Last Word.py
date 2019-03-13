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
if __name__=='__main__':
    s=Solution()
    s.lengthOfLastWord("W ")