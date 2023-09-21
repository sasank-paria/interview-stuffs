'''
The key process in quickSort is a partition(). 
The target of partitions is to place the pivot
(any element can be chosen to be a pivot) at its correct 
position in the sorted array and put all smaller elements 
to the left of the pivot, and all greater elements to the right of the pivot.

Partition is done recursively on each side of 
the pivot after the pivot is placed in its correct
position and this finally sorts the array.
'''

def quicksort(numbers):

    if len(numbers)<=1:
        return numbers
    else:
        pivot = numbers.pop()

    lower_elements = []
    greater_elements=[]

    for x in numbers:
        if x < pivot:
            lower_elements.append(x)

        else:
            greater_elements.append(x)
    
    return quicksort(lower_elements) + [pivot] + quicksort(greater_elements)


numbers = [5,6,7,8,9,8,7,6,5,6,7,8,9,0]
print(quicksort(numbers))


