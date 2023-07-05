def search(self, nums: list[int], target: int) -> int:
    l = 0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2
        if nums[mid] < target:
            #search in right half of the array
            l=mid+1
        elif nums[mid]>target:
            #search in left half of the array
            r=mid-1
        else:
            return mid
    return -1
