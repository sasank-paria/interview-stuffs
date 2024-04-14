# Problem Statement: Given an array of N integers, 
# write a program to add an array element at the beginning, end, and at a specific position.

# Example:
# Input: N = 5, array[] = {1,2,3,4,5}
# insertbeginning(6)
# insertending(7)
# insertatpos(8,4)
# Output: 6,1,2,8,3,4,5,7
# Explanation: 6 is added at the beginning and 7 is added at the end and 8 is added at position 4 


def func(arr):
    def insertbeginning(a):
        arr.insert(0,a)               #used to insert at any position  insert(position,element)
        # print(arr)
    insertbeginning(6)

    def insertending(b):
        arr.append(b)
    insertending(7)

    def insertatpos(c,d):
        arr.insert(d-1,c)
        print(arr)
    insertatpos(8,4)



arr = [1,2,3,4,5]
func(arr)