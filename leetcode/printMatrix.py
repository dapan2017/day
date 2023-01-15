class Solution:
    def spiralOrder(self , matrix: list[list[int]]) -> list[int]:
        res =[]
        if len(matrix) ==0:
            return res
        row = len(matrix)
        col = len(matrix[0])
        size = (min(row,col)+1)//2 
        for i in range(size):
            for j in range(i,col - i):
                res.append(matrix[i][j])
            for j in range(i+1,row - i):
                res.append(matrix[j][col - i - 1])
            for j in range(i+1,col - i ):
                if (row-1)-i>i:
                    res.append(matrix[row - i - 1][col-i -j])
            for j in range(i+1,row - 1- i):
                if i<col-1-i:
                    res.append(matrix[row - 1 -j][i])
        return res

