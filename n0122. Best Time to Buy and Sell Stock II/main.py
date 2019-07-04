// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices)==0:
            return 0
        MMax=0
        buy=0
        buy_m=prices[0]
        for index,value in enumerate(prices):
            if index<len(prices)-1 and value<prices[index+1]:
                    MMax+=(prices[index+1]-value)
        return MMax
