
while True:
	s = int(input("Height: "))
	if  s > 0:
		break
	else:
		print("Enter a positive number")

for i in range(s):

	# print spaces
	print(" " * (s-i-1), end="")
	# print hashes
	print("#" * (i+1), end="")
	print(" "*2, end="")
	# print hashes
	print("#" * (i+1), end="")
	# print a newline
	print()
