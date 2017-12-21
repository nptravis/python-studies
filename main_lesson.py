

# def main():
# 	print ("First Module's Name: {}".format(__name__))

# # asks, is this module being run directly or imported, if imported won't run what is inside the main method
# if __name__ == '__main__': 
# 	main()

# if __name__ == '__main__':
# 	print ("Run Directly")
# else:
# 	print ("Run from import")

print("This will always be run")

def main():
	print("Run from main module")


if __name__ == '__main__':
	main()