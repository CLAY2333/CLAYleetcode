// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def strStr(self, haystack, needle):
        if(needle==None):
            return 0
        return haystack.find(needle)
