// Author: CLAY2333 @ https://github.com/CLAY2333/CLAYleetcode
class Solution:
    def intToRoman(self, num: int) -> str:
        re=''
        num_list=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        lma_list=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        for i in num_list:
            re+=lma_list[num_list.index(i)]*int(num/i)
            num-=i*int(num/i)
        return re
