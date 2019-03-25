// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s==' ':
            return 1
        max_len=0
        Max=0
        index=0
        Len=len(s)
        re=''
        temp=''
        for i in range(len(s)):
            if s[index] not in re:
                re+=s[index]
                max_len+=1
                index += 1
            else:
                index-=max_len
                while(len(list(set(list(s[index+1:index+max_len+1]))))!=max_len):
                    if(index>Len-max_len-1):
                        break
                    index+=1
                re=s[index+1:index+max_len+1]
                index+=max_len+1
            if (max_len > Max):
                Max = max_len
            if(index>Len-1):
                break
        return Max
