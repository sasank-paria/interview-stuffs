
arr = [8,5,4,7,6,2,10]

for x in range(0,len(arr)):
    for y in range(0,len(arr)-i-1):
        if arr[y]>arr[y+1]:
            arr[y],arr[y+1]=arr[y+1],arr[y]

print(arr)
