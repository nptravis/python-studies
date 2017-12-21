import sys

## print out a command line argument
# if len(sys.argv) == 2:
# 	print("hello, {}".format(sys.argv[1]))
# else:
# 	print("hello world")

## print all command line arguments
# for i in range(len(sys.argv)):
# 	print(sys.argv[i])

## print each character of command line argument one at a time
for s in sys.argv:
	for c in s:
		print(c)
	print()

