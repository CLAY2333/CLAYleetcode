// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def generateMatrix(self, n: int) -> list:
        if(n==0):
            return []
        su=0
        re=[]
        index_x=0
        index_y=0
        num_index=0
        re_num=1
        walker=[[0 for i in range(n)] for i in range(n)]
        while(num_index<n*n):
            if(index_x<n and index_y<n and walker[index_x][index_y]==0):
                walker[index_x][index_y]=re_num
                re_num+=1
                num_index+=1
            else:
                if (su == 0):
                    index_y -= 1
                elif (su == 1):
                    index_x -= 1
                elif (su == 2):
                    index_y += 1
                elif (su == 3):
                    index_x += 1
                su=(su+1)%4
            if(su==0):
                index_y+=1
            elif(su==1):
                index_x+=1
            elif(su==2):
                index_y-=1
            elif(su==3):
                index_x-=1
        return walker

