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