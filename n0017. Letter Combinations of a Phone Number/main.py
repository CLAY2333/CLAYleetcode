// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def letterCombinations(self, digits: str) -> list:
        if(len(digits)==0):
            return []
        D={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits) == 1:
            return list(D[digits[0]])
        re=[]
        List_str=list(digits)
        for i in D[digits[0]]:
            re.append(i)
        List_str=List_str[1:len(List_str)]
        for index_L,value_L in enumerate(List_str):
            if (value_L != 1):
                temp = []
                for index, value in enumerate(re):
                    for i in D[value_L]:
                        temp.append(value + i)
                re = temp.copy()
            else:
                pass
        return re
