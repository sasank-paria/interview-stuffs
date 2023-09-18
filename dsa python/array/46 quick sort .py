
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


