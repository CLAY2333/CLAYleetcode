// Author: Netcan @ https://github.com/netcan/Leetcode-Rust
class Solution(object):
    def strStr(self, haystack, needle):
        if(needle==None):
            return 0
        return haystack.find(needle)
