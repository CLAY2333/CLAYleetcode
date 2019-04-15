// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        temp_value=0
        times=0
        for index_x,value_x in enumerate(matrix):
            times=0
            for index_y,value_y in enumerate(value_x):
                if(times>=n-index_x-1):
                    break
                else:
                    x=n-1-index_x-index_y
                    temp_value=matrix[index_x][index_y]
                    matrix[index_x][index_y]=matrix[x+index_x][x+index_y]
                    matrix[x+index_x][x+index_y]=temp_value
                    times+=1
        times=0
        for index_x,value_x in enumerate(matrix):
            if times>=n-index_x:
                break
            temp_value=value_x
            matrix[index_x]=matrix[n-index_x-1]
            matrix[n - index_x-1]=temp_value
            times+=1
