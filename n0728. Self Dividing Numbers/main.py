// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        List=[]
        for i in range(left,right+1):
            temp_str=str(i)
            index=0
            if '0' in temp_str:
                continue
            for j in range(len(temp_str)):
                if(i%int(temp_str[j])!=0):
                    index=1
                    break
            if index==0:
                List.append(i)
            index=0
        return List
