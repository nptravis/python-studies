# Variables
a = 3
x = 54
string = "hello, world"
string = 'single qoutes is also acceptable'

# Conditionals
if y < 15 or x == 54:
	return True

if y < 43 and z == 32:
	return True
else:
	return False

if name == 'Nic':
	return True
elif not name == 'Nic':
	return False

if bool1 or bool2:
	return True

if bool1 and bool2:
	return False



letters_only = True if input().isalhpa() else False

# Loops
counter = 0
while counter < 100:
	print(counter) # adds \n by default
	counter += 1 # can't use counter ++

for x in range(100):
	print(x)

for x in range(0, 100, 2): #(start, end, increment size)
	print(x) # 0, 2, 4, etc...not 100

# Arrays/lists
nums = []

nums = [1,2,3,4]

nums = [x for x in range(500)] # 500 elements in list, 0-499

nums = list() # same as num = []

nums = [1,2,3,4]
nums.append(5) # [1,2,3,4,5]
nums.insert(4,5) # inserts in index 4, the element 5 [1,2,3,4,5]
nums[len(nums):] = [5,6] # attaches list to the end of other list [1,2,3,4,5,6]

# Tuples
## an ordered, immutable set of data

## a list of tuples
presidents = [
	("George Washington", 1789), # a single tuple
	("John Adams", 1797),
	("Thomas Jefferson", 1801),
	("James Madison", 1809)
]

for prez, year in presidents:
	print("In {1}, {0} took office".format(prez,year))
	# In 1789 George Washington took office
	# In 1797 John Adams took office
	# etc..

# Dictionaries - unordered key value pairs
pizzas = {
	"cheese": 10, # key/value pair
	"pepperonni": 11,
	"veggie": 12,
	"chicken": 14
}

pizzas["chicken"] = 13 # now chicken is 13, not 14
if pizzas["veggie" < 15]
	# do something
pizzas["bacon"] = 15 # adds a new key/value pair 

for pie in pizzas:
	print(pie)
	# cheese
	# pepperoni
	# veggie
	# chicken
	# bacon

for pie, price in pizzas.items():
	print(price) # doesn't keep them in order
	# 10
	# 15
	# 12
	# 13
	# 11

for pie, price in pizzas.items():
	print("A whole {} costs ${}".format(pie, price))

# this would print the same thing
print("A whole " + pie + "costs $" + str(price))

# Functions
def square(x):
	return x * x
	return x ** 2 # also returns x squared

def main()

if __name__ == "__main__": 
	main() # used to separate the portion of code which should be executed from the portions of code which define functionality


# Objects

# similar to structs in C
# methods are functions that can be called upon objects and their properties

object.method()

# class keyword defines objects
# class requires a constructor, an initialization function, which sets the starting values of the properties of the object
# self reference to what object the method is called

class Student():

	def __init__(self, name, id): # always self first
		self.name = name
		self.id = id

	def changeID(self, id):
		self.id = id

	def print(self):
		print("{} - {}".format(self.name, self.id))

# so
jane = Student("Jane", 10)
jane.print()
jane.changeID(11)
jane.print()

# Including Files

import sys
import cs50

# Print

print("hello, world")

print("name: ", end="") # excludes newline

print("Mookie" * 50)

print() # print a newline

# Misc

#!/usr/bin/env python3
--include line at top of file to run using './' method

# But also need to change permissions for it to work
chmod a+x <file>

# in order to tell flask how to import file
$ export FLASK_APP=microblog.py

# create virtual environment folder in project
$ python3 -m venv venv
# activate virtual environment
$ source venv/bin/activate

# References
https://www.python.org/dev/peps/pep-0008/
https://docs.python.org/3/reference/index.html
https://docs.python.org/3/library/
https://docs.python.org/3/tutorial/index.html


