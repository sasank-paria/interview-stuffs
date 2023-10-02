def longestSubarrayWithSumK(a: [int], k: int) -> int:
    

    currsum = 0
    max_arr = 0
    arr_len = 0
    n = len(a)

    for x in range(0,n):
        currsum = currsum + a[x]
        arr_len +=1

        if a[x] == k :
            max_arr = 1

        if currsum == k:
            max_arr = max(arr_len,max_arr)
        
        if currsum > k :
            currsum = 0
            arr_len = 0

    return max_arr
    