// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        re = []
        Len = len(T)
        T_hash = {}
        T_re = list(reversed(T))
        Stack = []

        for index, value in enumerate(T_re):
            if len(Stack) == 0:
                re.append(0)
                Stack.insert(0, index)
                T_hash[index] = value
            else:
                while len(Stack) != 0 and T_hash[Stack[0]] <= value:
                    del Stack[0]
                if len(Stack) == 0:
                    re.append(0)
                    Stack.insert(0, index)
                    T_hash[index] = value
                else:
                    re.append(index - Stack[0])
                    Stack.insert(0, index)
                    T_hash[index] = value
        return list(reversed(re))
