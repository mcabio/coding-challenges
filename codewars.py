# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28
# Note: this kata uses strict construction as shown in the 
# description and the examples, you can read more about it here

def century(year):
    cent = year - 1
    time = cent // 100
    hundred = time + 1
    return hundred


year = 1900
result = century(year)
print(result)

# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied 
# array will not be empty.

def find_smallest_int(arr):
    # loop over the integers in the array.

    smallest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr = [34, -345, -1, 100]
result = find_smallest_int(arr)
print(result)


# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    """"Reverse the string parameter"""
    reverse_string = string[::-1]
    return reverse_string

string = 'palindrome'
result = solution(string)
print(result)


# Fake Binary

# Given a string of digits, you should replace any digit below 5 
# with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string
# This was solved but it was challenging

def fake_bin(x):
    """Return a 0 if integer is < 5 and a 1 if it's > 5"""
    # Take the string and turn it into an integer
    list_x = [int(num) for num in str(x)] # list comprehension
    binary = []
    
    for num in list_x:
        if num < 5:
            binary.append(0)
        else:
            binary.append(1)
    
    numbers_str = [str(i) for i in binary]
    string_binary = "".join(numbers_str)
    return string_binary



x = "4848484848484848"
result = fake_bin(x)
print(result)


# Removing Elements

# Take an array and remove every second element from the array. 
# Always keep the first element and start removing with the next element.

# Example:
# ["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

# None of the arrays will be empty, so you don't have to worry about that!

def remove_every_other(my_list):
    """Remove every second element in the array"""
    # Create a function, loop over the length of the array,
    # To remove every other element of the array, use indexing and then 
    # .pop
    # return array without the elements

    return my_list[::2]


my_list = ["Keep", "Remove", "Keep", "Remove", "Keep", "Remove", "Keep", "Remove"]
result = remove_every_other(my_list)
print(result)



# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

# Solved

def number_to_string(num):
    """Turn an integer into a string"""
    return str(num)


num = 4444
result = number_to_string(num)
print(result)



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


