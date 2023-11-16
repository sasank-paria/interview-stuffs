'''73.

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''


def setZeroes(self, matrix: List[List[int]]) -> None:

        def setrow(matrix,i,m,n):
            for j in range(n):
                if matrix[i][j] != 0 :
                    matrix[i][j] = 'a'

        def setcol(matrix,j,m,n):
            for i in range(m):
                if matrix[i][j]!=0:            
                    matrix[i][j]= 'a' 

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    setrow(matrix,i,m,n)
                    setcol(matrix,j,m,n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]== 'a' :
                    matrix[i][j] = 0
