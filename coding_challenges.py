# Complete the square sum function so that it squares each number passed 
# into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1^2 + 2^2 + 1^2 = 9

def square_sum(numbers):
    """Function that squares each number passed into it and then 
    adds them together"""
    # function takes in list of integers
    # function outputs an integer
    # each integer in the list will be squared
    # then each squared integer will be added to each other for the output.
    total = 0  # start off with zero first so the for loop has something to add into.
    for num in numbers: # loops through each number on the list
        total += num ** 2  # 0 + each number squared by 2
    print(total)
    

numbers = [4, 4, 4, 4]
square_sum(numbers)
# this should output 64