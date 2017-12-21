import sys

def main():
	x = 1
	y = 2

	print("x is {}".format(x))
	print("y is {}".format(y))
	print("Swapping...")
	x,y = y,x # WOW!!!! returns a tuple
	print("Swapped.")
	print("x is {}".format(x))
	print("y is {}".format(y))



if __name__ == "__main__":
	main()