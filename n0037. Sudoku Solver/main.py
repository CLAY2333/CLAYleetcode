// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
import copy
class Solution:
    def solveSudoku(self, board:list) -> None:

        """
        Do not return anything, modify board in-place instead.
        """
        def place(value,row_num,col_num):
            row[row_num][value]=1
            col[col_num][value]=1
            box_num=(row_num//3)*3+col_num//3
            box[box_num][value]=1
            board_list[row_num][col_num]=value

        def clean_place(value,row_num,col_num):
            row[row_num][value]=0
            col[col_num][value]=0
            box_num=(row_num//3)*3+col_num//3
            box[box_num][value]=0
            board_list[row_num][col_num] = 0
        def loop_sudu(row_num,col_num,res):
            if(board_list[row_num][col_num]==0):
                for value in range(1,10):
                    if(row[row_num][value]!=1 and col[col_num][value]!=1 and box[(row_num//3)*3+col_num//3][value]!=1):
                        place(value,row_num,col_num)
                        next_row=row_num
                        next_col=col_num
                        next_col+=1
                        if next_col>=9:
                            next_col=0
                            next_row+=1
                        if next_row>=9:
                            res=copy.deepcopy(board_list)
                            return res
                        res=loop_sudu(next_row,next_col,res)

                        clean_place(value,row_num,col_num)
            else:
                col_num += 1
                if col_num >= 9:
                    col_num = 0
                    row_num += 1
                if row_num >= 9:
                    res=copy.deepcopy(board_list)
                    return res
                res=loop_sudu(row_num, col_num,res)
            return res
        row=[[0 for i in range(10)] for n in range(9)]
        col=[[0 for i in range(10)] for n in range(9)]
        box=[[0 for i in range(10)] for n in range(9)]
        board_list=[[0 for i in range(len(board[0]))] for i in range(len(board))]
        for index,value in  enumerate(board):
            for i,v in enumerate(value):
                if v!=".":
                    place(int(v),index,i)
        res=[]
        re=loop_sudu(0,0,res)
        for index,value in  enumerate(board):
            for i,v in enumerate(value):
                if v==".":
                    board[index][i]=str(re[index][i])

