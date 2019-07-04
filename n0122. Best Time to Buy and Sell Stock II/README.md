
### Best Time to Buy and Sell Stock II :star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii)
- 执行时间/Runtime: 64 ms 
- 内存消耗/Mem Usage: 13.6 MB
- 通过日期/Accept Datetime: 2019-07-04 22:09
```python
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

```
