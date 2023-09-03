'''coding ninja from striver 

second largest and second smallest element
'''

def getSecondOrderElements():
    arr = [4,5,3,6,7]
    n= 5
    arr.sort()
    res = []

    second_smallest = arr[1]
    second_largest = arr[-2]

    res.append(second_smallest)
    res.append(second_largest)
    print(res)
    return res

getSecondOrderElements()





