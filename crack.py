import crypt
import sys





def main():
	while
	

	# Get hash from user
	try:
		p = sys.argv[1]
	except Exception:
		print("Error, Usage: program.py <hash>")
		exit(1)

	salt = p[0] + p[1]
	password = ['A']
	string_pass = ''.join(password)


  # crack the hash
  def loop(password):
		while True:
		# check all lower case and upper case letters
			if crypt.crypt(string_pass, salt) == p:
				return string_pass = ''.join(password)
			elif password < 'Z':
				password = chr(ord(password) + 1)
			else:
				if password == 'Z':
					password = 'a'
				else:
					password = chr(ord(password) + 1)
			string_pass = ''.join(password)


	
  # print the cracked password
	print(string_pass)


if __name__ == "__main__":
	main()
	exit(0)




# -crypt.crypt(word, salt)
# hashing a word will alwyas return the same hash
# crack it
# usage: crack password
# get hashed password
# -commnd line arg

