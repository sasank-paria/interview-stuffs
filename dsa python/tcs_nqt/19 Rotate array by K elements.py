# Example 1:
# Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
# Output: 6 7 1 2 3 4 5
# Explanation: array is rotated to right by 2 position .

# Example 2:
# Input: N = 6, array[] = {3,7,8,9,10,11} , k=3 , left 
# Output: 9 10 11 3 7 8
# Explanation: Array is rotated to right by 3 position.


#easily solve ho gya
def func(arr,k,direction):

    if direction == 'right' :
        temp = 0
        for x in range(k):
            temp = arr.pop()
            arr.insert(0,temp)
        print(arr)
    
    if direction == 'left':
        temp = 0
        for x in range(k):
            temp = arr.pop(0)     #pop(index)
            arr.append(temp)
        print(arr)


arr = [3,7,8,9,10,11]
k = 3
direction = 'left'
func(arr,k,direction)