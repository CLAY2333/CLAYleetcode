// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def loop(self,board,word,index_x,index_y,stu,rout):
        if(stu[0]==1):
            return 0
        if(board[index_x][index_y]==word[0]):
            rout[index_x][index_y]=1
            if (len(word) == 1):
                stu[0] = 1
                return 0
            if(index_y+1<len(board[0]) and rout[index_x][index_y+1]!=1):
                self.loop(board,word[1:],index_x,index_y+1,stu,rout)
            if (index_y - 1 >= 0 and rout[index_x][index_y-1]!=1):
                self.loop(board, word[1:], index_x, index_y -1, stu,rout)
            if(index_x+1<len(board) and rout[index_x+1][index_y]!=1):
                self.loop(board,word[1:],index_x+1,index_y,stu,rout)
            if (index_x - 1 >=0 and rout[index_x-1][index_y]!=1):
                self.loop(board, word[1:], index_x - 1, index_y, stu, rout)
            rout[index_x][index_y]=0
    def exist(self, board: list, word: str) -> bool:
        stu=[0]
        for index_x,value_x in enumerate(board):
            for index_y,value_y in enumerate(value_x):
                if value_y==word[0]:
                    rout = [[0 for i in range(len(board[0]))] for i in range(len(board))]
                    self.loop(board,word,index_x,index_y,stu,rout)

        if stu[0]==1:
            return True
        else:
            return False
