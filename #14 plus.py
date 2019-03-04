class Solution(object):
    def longestCommonPrefixtwo(self,strs):
        len_strs1 = len(strs[0])
        len_strs2 = len(strs[1])
        record = [[0 for i in range(len_strs2 + 1)] for j in range(len_strs1 + 1)]
        maxnum = 0
        p = 0
        for i in range(len_strs1):
            for j in range(len_strs2):
                if (strs[0][i] == strs[1][j]):
                    record[i + 1][j + 1] = record[i][j] + 1
                    if (record[i + 1][j + 1] > maxnum):
                        maxnum = record[i + 1][j + 1]
                        p = i
        strss = ""
        if (p == 0 and  maxnum == 0):
            return strss
        return strs[0][p + 1 - maxnum:p + 1]
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        len_strs=len(strs)
        if(len_strs==0):
            return ""
        if(len_strs==1):
            return strs[0]
        if(len_strs==2):
            return  self.longestCommonPrefixtwo([strs[0],strs[1]])
        commonstrs= self.longestCommonPrefixtwo([strs[0],strs[1]])
        print(commonstrs)
        for i in range(len(strs)-2):
            commonstrs=self.longestCommonPrefixtwo([commonstrs,strs[i+2]])
        return commonstrs

if __name__ == '__main__':
    s=Solution()
    print(s.longestCommonPrefix(["c","acc","ccc"]))