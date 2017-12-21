
# f = open('testfile.txt')

try:
	# f = open('test_file.txt')
	# var = bar_var
	f = open('corrupt_file.txt')
	if f.name == 'corrupt_file.txt':
		raise Exception
	# pass
# except Exception: # will catch many other exception errors
# 	print("Sorry, this file does not exist")
# 	# pass
# except FileNotFoundError: # make sure this one is on top
# 	print("Sorry, this file does not exist")
# except Exception:
# 	print("Sorry, something went wrong")
except FileNotFoundError as e: 
	print(e)
except Exception as e:
	# print(e)
	print("Error!")

else: # only runs if we don't throw an exception
	print(f.read())
	f.close()
finally: # always runs even if there is an exception, like shutting down a database
	print("Executing Finally...")
