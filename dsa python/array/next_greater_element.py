'''
Input: arr[] = [ 4 , 5 , 2 , 25 ]
output:
5 25 25 -1
'''

arr = [ 4 , 5 , 2 , 25 ]
greater = []

for x in range(0,len(arr)):
    for y in range (x+1,len(arr)):
        if arr[y] > arr[x]:
            greater.append(arr[y])
            break

        
 # If no element is found to be greater than the current one then append a negative value (-
if arr[-1]:
        greater.append(-1)
   

print(greater)