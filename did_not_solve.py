

# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array or list ( depending on language ).

# Examples
# count_by(1,10) should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) should return [2,4,6,8,10]

# This function uses a list comprehension to generate the 
# first n multiples of x. It iterates from 1 to n (inclusive) and 
# multiplies each number by x, appending the result to the list. 
# It returns the list containing the multiples.

# Needed help solving.

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [x * i for i in range(1, n + 1)]

# Without list comprehension:

def count_by(x, n):
    multiples = []
    for i in range(1, n + 1):
        multiples.append(x * i)
    return multiples

count_by(2, 8)
# This should be [2, 4, 6, 8, 10, 12, 14, 16]





# Complete the square sum function so that it squares each number passed 
# into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1^2 + 2^2 + 1^2 = 9

# function takes in list of integers
# function outputs an integer
# each integer in the list will be squared
# then each squared integer will be added to each other for the output.

# Needed help solving

def square_sum(numbers):
    """Function that squares each number passed into it and then 
    adds them together"""
    total = 0  # start off with zero first so the for loop has something to add into.
    for num in numbers: # loops through each number on the list
        total += num ** 2  # 0 + each number squared by 2
    print(total)

numbers = [4, 4, 4, 4] # this should output 64
square_sum(numbers)