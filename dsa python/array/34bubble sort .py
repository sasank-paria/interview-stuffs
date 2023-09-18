
arr = [8,5,4,7,6,2,10]

for x in range(0,len(arr)):
    for y in range(x+1,len(arr)):
        if arr[x]>arr[y]:
            arr[x],arr[y]=arr[y],arr[x]

print(arr)