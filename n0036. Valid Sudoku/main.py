// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def isValidSudoku(self, board: list) -> bool:
        row=[{} for i in range(9)]
        column = [{} for i in range(9)]
        box = [{} for i in range(9)]
        for index_row,value_row in enumerate(board):
            for index_column,value in enumerate(value_row):
                if not (row[index_row].get(value) and value!='.'):
                    row[index_row][value]=1
                else:
                    return False
                if not (column[index_column].get(value) and value!='.'):
                    column[index_column][value]=1
                else:
                    return False
                box_num=(index_row//3)*3+index_column//3
                if not (box[box_num].get(value) and value!='.'):
                    box[box_num][value]=1
                else:
                    return False
        return True
