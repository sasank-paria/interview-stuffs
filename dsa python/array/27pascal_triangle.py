'''
suppose N = 5
output:

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Here for the third row, you will see that the second element is the summation of the 
above two-row elements i.e. 2=1+1, and similarly for row three 3 = 1+2 and 3 = 1+2.
'''

# to solve this assume zeroes at the ending and beginneing of the rows

no_rows = 5

res = [[1]]

for i in range((no_rows)-1):
    temp = [0]+ res[-1]+[0]
    rows = []
    for j in range(len(res[-1])+1):
        rows.append(temp[j]+temp[j+1])
    res.append(rows)

print(res)