// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
from itertools import permutations
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        re=[]
        now_re=[]
        nums=[]
        times=[0]
        k-=1
        re=''
        for i in range(1,n+1):
            nums.append(i)
        for i in range(n):
            epoch=math.factorial(n-1)
            re+=str(nums[k//epoch])
            nums.pop(nums.index(nums[k//epoch]))
            k=k%epoch
            n-=1
        return re
