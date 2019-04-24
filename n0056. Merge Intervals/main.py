// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def merge(self, intervals: list) -> list:
        if len(intervals) <= 1:
            return intervals
        re=[]
        D={}
        intervals.sort()
        print(intervals)
        loop_value=intervals.copy()
        for index,value in enumerate(loop_value):
            now_index=intervals.index(value)
            pre_index=now_index-1
            if not (D.get(str(value[0])+str(value[1]))):
                D[str(value[0])+str(value[1])]=1
            else:
                intervals.pop(now_index)
                continue
            if index==0:
                continue
            if intervals[now_index][0]<=intervals[pre_index][1]:
                if(intervals[now_index][1]>=intervals[pre_index][1]):
                    intervals[pre_index][1]=intervals[now_index][1]
                intervals.pop(now_index)
        return intervals
