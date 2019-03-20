// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        index_1=1
        index_2=0
        temp=[0]*len(A)
        for i in A:
            if i%2==0:
                temp[index_2]=i
                index_2+=2
            else:
                temp[index_1]=i
                index_1+=2
        return temp
