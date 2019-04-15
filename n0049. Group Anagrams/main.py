// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def groupAnagrams(self, strs:list) -> list:
        D={}
        re=[]

        for index,value in enumerate(strs):
            temp_value=value
            now_value=''.join(sorted(temp_value))
            if D.get(now_value)==None:
                D[now_value]=len(re)
                re.append([value])
            else:
                re[D.get(now_value)].append(value)
        return re
