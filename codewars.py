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



# We need a function that can transform a string into a number. 
# What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every 
# string is a perfectly valid representation of an integral number.

# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

# Solved

def string_to_number(s):
    """Convert string to numbers"""
    # Function will take a string
    numbers = int(s)
    return numbers

# This could also be done:
# def string_to_number(s):
#     return int(s)   

result = string_to_number("4444")
print(result)



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


# Consider an array/list of sheep where some sheep may be missing 
# from their place. We need a function that counts the number of 
# sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined
# Solved

def count_sheeps(sheep):
  """Counts sheep (True) and returns an integer"""
  # Write a function that will loop over an array that will count
  # all the true values and return its number. 
  # Consider edge cases such as null or undefined. 
  total = 0
  for sleep in sheep:
    if sleep == True:
      total += 1

  return total


# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"
# Names given are always valid strings.
# Solved

def are_you_playing_banjo(name):
    """Does the name start with the letter R?"""
    if name[0] == "r":
      print (f"{name} plays banjo")

    elif name[0] == "R":
       print (f"{name} plays banjo")

    else: 
       print (f"{name} does not play banjo")
    
# Another way to write it:

def are_you_playing_banjo(name):
    """Does the name start with the letter R?"""
    if name[0] == "r" or name[0] == "R":
        print(f"{name} plays banjo")
    else: 
        print(f"{name} does not play banjo")


# Convert number to reversed array of digits

# Given a random non-negative number, you have to 
# return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    """Return numbers into an array reversed"""
    r = [int(x) for x in str(n)]
    r.reverse()
    print (r)

# Shorter version

def digitize(n):
    return([int(x) for x in str(n)[::-1]])


# Find the smallest integer in the array

# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array 
# will not be empty.

# Needed help solving

       
def find_smallest_int(arr):
    """Return smallest integer in array"""
    # loop over the length of the array
    # index 0 will be the smallest one
    # if the loop comes across a number smaller than the one at index[0]
    # That will replace the old one and so on and so forth.

    smallest = arr[0] # First number in the array is considered the smallest

    for num in arr[1:]: # For loop iterates over the array starting at 
                        # the second integer.
        if num < smallest:  # If num is less than the smallest, replace
                            # the integer in the variable with new num
                            # And continue to do so until it loops 
                            # over the whole array
            smallest = num

    print(smallest)
        

arr = [34, -345, -1, 100]
find_smallest_int(arr)