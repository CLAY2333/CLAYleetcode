// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def maxProfit(self, prices: list) -> int:
        if(len(prices)==0):
            return 0
        money=[[0]*2 for i in range(len(prices))]
        money[0][0]=0
        MMax=0
        money[0][1]=prices[0]
        for i in range(1,len(prices)):
            if(money[i-1][1]>prices[i]):
                money[i][1]=prices[i]
            else:
                money[i][1]=money[i-1][1]
            money[i][0]=max(money[i-1][0],prices[i]-money[i][1])
            if(money[i][0]>MMax):
                MMax=money[i][0]
        return MMax
