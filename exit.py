import sys


if len(sys.argv) != 2:
	print("missing command-line argument")
	exit(1) # use echo $? to see the return value

print("hello, {}".format(sys.argv[1]))
exit(0) # use echo $? to see the return value