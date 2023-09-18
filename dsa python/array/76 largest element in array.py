'''coding ninja from striver

'''


def largestElement():

    arr = [5 ,9, 3, 4, 8, 4, 3, 10 ]
    n = 6
    max = 0
    for x in range(len(arr)):
        if(arr[x]>max):
            max = arr[x]
    print(max)
    return max


largestElement()
