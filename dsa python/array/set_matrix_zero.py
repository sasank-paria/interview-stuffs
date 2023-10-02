#brute force approach


def setrow(matrix,i,m,n):
    for j in range(n):
       if matrix[i][j] != 0 :
           matrix[i][j] = -1

def setcol(matrix,j,m,n):
    for i in range(m):
        if matrix[i][j]!=0:            
            matrix[i][j]= -1        


def setZeroes( matrix):

    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                setrow(matrix,i,m,n)
                setcol(matrix,j,m,n)

    for i in range(m):
        for j in range(n):
            if matrix[i][j]== -1 :
                matrix[i][j] = 0
    print(matrix)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
    
# Output: [[1,0,1],[0,0,0],[1,0,1]]