'''1491

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

Example 2:
Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
'''

def average():
    salary =  [4000,3000,1000,2000]
    salary.sort()
    
    addition = 0
    for x in range(1,len(salary)-1):
        addition = addition + salary[x]
    
    len_of_arr_for_avg = len(salary) - 2
    
    average_salary = addition / len_of_arr_for_avg
    
    print(average_salary)

average()