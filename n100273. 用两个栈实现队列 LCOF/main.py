// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class CQueue:

    def __init__(self):
        self.A=[]
        self.B=[]
    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B:
            return self.B.pop()
        elif self.A:
            self.B=self.A.copy()
            self.A=[]
            self.B.reverse()
            return self.B.pop()
        else:
            return -1
