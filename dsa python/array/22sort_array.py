'''
You have been given an integer array/list(ARR) of size 'N'. 
It only contains 0s, 1s and 2s. Write a solution to sort this array/list.
'''

# use two pointer technique

arr = [0 ,1 ,2, 2, 1,0]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]  #swiping of nos in an array

print(arr)