
# Import any required module/s
import math

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):

    distance = 0
    
    dist = math.sqrt ((x1-x2)**2 + (y1-y2)**2)
    
    return dist


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the x1, y1, x2 and y2 values
    x1 = input()
    x2 = input()
    y1 = input()
    y2 = input()
    
    
    # Once you have all 4 values, call the compute_distance function to find Euclidean distance
    compute_distance(x1, y1, x2, y2)