// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def Loop(self,candidates,target,now_index,re:list,now_list:list):
        if(target==0):
            re.append(now_list.copy())
        if(target<candidates[0]):
            return 0
        for index,value in enumerate(candidates):
            if(value>target):
                break
            if(value<candidates[now_index]):
                continue
            now_list.append(value)
            self.Loop(candidates,target-value,index,re,now_list)
            now_list.pop()

    def combinationSum(self, candidates: list, target: int) -> list:
        if len(candidates)==0:
            return []
        candidates=sorted(candidates)
        now_list=[]
        index=0
        re=[]
        self.Loop(candidates,target,index,re,now_list)
        return re
