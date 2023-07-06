'''
Input: N = 4, pages[] = {12, 34, 67, 90}, M = 2

Output: 113

Explanation: There are 2 number of students. Books can be distributed in following combinations: 

[12] and [34, 67, 90] -> Max number of pages is allocated to student ‘2’ with 34 + 67 + 90 = 191 pages
[12, 34] and [67, 90] -> Max number of pages is allocated to student ‘2’ with 67 + 90 = 157 pages 
[12, 34, 67] and [90] -> Max number of pages is allocated to student ‘1’ with 12 + 34 + 67 = 113 pages
Of the 3 cases, Option 3 has the minimum pages = 113.
'''

