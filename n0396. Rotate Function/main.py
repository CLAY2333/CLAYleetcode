// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        temp_sum=0
        index=0
        sum_list=sum(A)
        for i in A:
            temp_sum += index * i
            index += 1
        max=temp_sum
        for i in range(len(A)-1):
            temp_sum-=A[-1]*(len(A))
            temp_sum+=sum_list
            if temp_sum >max:
                max=temp_sum
            A.insert(0,A.pop())
        return max

if __name__=='__main__':
    S=Solution()
    A=[4, 3, 2, 6]
    print(S.maxRotateFunction(A))
