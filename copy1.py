import sys

print("s: ", end="")
s = input()
if s == None:
	exit(1)

t = s.capitalize()

print("s: {}".format(s))
print("t: {}".format(t))

exit(0)