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
