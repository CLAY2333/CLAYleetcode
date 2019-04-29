// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def subsets(self, nums: list) -> list:
        re_t=0
        re_t_list=[]
        re=[]
        re_num=[]
        for i in range(pow(2,len(nums))):
            re_t_list.append(str(bin(re_t))[2::])
            re_t+=1
        print(re_t_list)
        for index,value in enumerate(re_t_list):
            for index_str,value_str in enumerate(value):
                if(value_str=='1'):
                    re_num.append(nums[len(value)-index_str-1])
            re.append(re_num)
            re_num=[]
        return re
