class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle==None):
            return 0
        return haystack.find(needle)
if __name__=='__main__':
    s=Solution()
    haystack = ""
    needle = "aa"
    num=s.strStr(haystack,needle)
    print(num)