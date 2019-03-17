// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)):
            sum+=value[s[i]]
        sum -= (s.count('IV') * 2)
        sum -= (s.count('IX') * 2)
        sum -= (s.count('XL') * 20)
        sum -= (s.count('XC') * 20)
        sum -= (s.count('CD') * 200)
        sum -= (s.count('CM') * 200)
        return sum
