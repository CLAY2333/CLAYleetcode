// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def loop(self,nums:list,re:list,now_re:list):
        for index,value in enumerate(nums):
            now_re.append(nums.pop(index))
            if(len(nums)==0):
                re.append(now_re.copy())
                now_re.pop(now_re.index(value))
                nums.insert(index, value)
                return 0
            self.loop(nums,re,now_re)
            now_re.pop(now_re.index(value))
            nums.insert(index,value)
    def permute(self, nums: list) -> list:
        re=[]
        now_re=[]
        self.loop(nums,re,now_re)
        return re
