// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        intervals.append(newInterval)
        self.intervals=intervals.sort()
        res=intervals.copy()
        for index,value in enumerate(intervals):
            if(index+1>=len(intervals)):
                continue
            if value[1]>=intervals[index+1][0]:
                if value[1]>intervals[index+1][1]:
                    intervals[index + 1][0]=value[0]
                    intervals[index + 1][1]=value[1]
                    del res[res.index(value)]
                else:
                    intervals[index + 1][0] = value[0]
                    del res[res.index(value)]
        return res
