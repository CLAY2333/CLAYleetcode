
### Reveal Cards In Increasing Order :star::star:
- 题目地址/Problem Url: [https://leetcode-cn.com/problems/reveal-cards-in-increasing-order](https://leetcode-cn.com/problems/reveal-cards-in-increasing-order)
- 执行时间/Runtime: 68 ms 
- 内存消耗/Mem Usage: 13.1 MB
- 通过日期/Accept Datetime: 2019-04-29 18:26
```python
// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        deck.sort(reverse=True)
        re=[]
        re.append(deck[0])
        deck.pop(0)
        for index,value in enumerate(deck):
            re.insert(0,re[-1])
            re.pop(-1)
            re.insert(0,value)
        return re

```
