# You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm. Return the total number of legs on your farm.

def animals(chickens, cows, pigs):
    chickens = chickens * 2
    cows = cows * 4
    pigs = pigs * 4
    # print (chickens + cows + pigs)
    return chickens + cows + pigs

animals(1,4,4)

# Write two functions:
# to_int() : A function to convert a string to an integer.
# to_str() : A function to convert an integer to a string.

def to_int(txt):
    txt = int(txt)
    return txt
	

def to_str(num):
    num = str(num)
    return num

# Create a function that takes a list of numbers. Return the largest number in the list.

def findLargestNum(nums):
	return max(nums)

# Create a function that takes a list and returns the difference between the smallest and biggest numbers.

def difference_max_min(lst):
    return max(lst) - min(lst)

# Create a function that takes a name and returns a greeting.

def hello_name(name):
    return ( "Hello " + name + "!")

# Create a function that takes two strings as arguments and return either True or False depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
  
def comp(txt1, txt2):
    if len(txt1) == len(txt2):
        return True
    else:
        return False

# Create a function that takes a number as its only argument and returns True if it's less than or equal to zero, otherwise return False.

def less_than_or_equal_to_zero(num):
    if num <= 0:
        return True
    else:
        return False

# Create a function that accepts a list and returns the last item in the list. The list can be either homogeneous or heterogeneous.

def get_last_item(lst):
	return lst[-1]

# Create a function that takes an integer and returns True if it's divisible by 100, otherwise return False.

def divisible(num):
    if num % 100 == 0:
        return True
    else:
        return False

# Create a function to concatenate two integer lists.

def concat(lst1, lst2):
    res = lst1 + lst2
    return res

# Create a function that returns the ASCII value of the passed in character.

def ctoa(char):
	return ord(char)

# Create a function that returns True if a string is empty and False otherwise.

def is_empty(s):
    if len(s) <= 0:
        return True
    else:
        return False

# Create a function that returns True if a string contains any spaces.

def has_spaces(txt):
    if '' in txt:
        return True
    else:
        return False

# Write a function to check if a list contains a particular number.

def check(lst, el):
    if el in lst:
        return True
    else:
        return False
    
# Create a function that determines whether or not it's possible to split a pie fairly given these three parameters:

# Total number of slices.
# Number of recipients.
# How many slices each person gets.
# The function will be in this form:

# equal_slices(total slices, no. recipients, slices each)

def equal_slices(total, people, each):
    if people * each <= total:
        return True
    else:
        return False

# Create a function that takes in a word and determines whether or not it is plural. A plural word is one that ends in "s".

def is_plural(word):
    if word[-1] == "s":
        return True
    else:
        return False

def is_plurals(word):
    if word.endswith('s'):
        return True
    else:
        return False

# Write a function that validates whether two strings are identical. Make it case insensitive.

def match(s1, s2):
    if s1.lower() == s2.lower():
        return True
    else:
        return False

# Create a function that takes a number as an argument and returns "even" for even numbers and "odd" for odd numbers.

def isEvenOrOdd(num):
    if num % 2 == 0:
        return 'even'
    else:
        return 'odd'

# Write a function that returns True if a dictionary is empty, and False otherwise.

def is_empty(dictionary):
    if len(dictionary) <= 0:
        return True
    else:
        return False

# Here's an image of four models. Some of the cubes are hidden behind other cubes. Model one consists of one cube. Model two consists of four cubes, and so on...

# Write a function that takes a number n and returns the number of stacked boxes in a model n levels high, visible and invisible.

def stack_boxes(n):
    return n * n

# Create a function that takes a list of elements and return the first and last elements as a new list.

def first_last(lst):
    first_and_last = [lst[0]] + [lst[-1]]
    return first_and_last

# Create a function that accepts a list of numbers and return both the minimum and maximum numbers, in that order (as a list).

def min_max(nums):
    return [min(nums)] + [max(nums)]


min_max([1, 2, 3, 4, 5]) # ➞ [1, 5]