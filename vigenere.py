import sys

def main():

	# variables
	try:
		key = sys.argv[1]
	except IndexError:
		print("Error! Usage: program.py <key>")
		exit(1)

	plaintext = ""
	while plaintext == "":
		plaintext = input("Input plaintext: ")
		if plaintext == "":
			print("Must add some plaintext!")

	key = key.lower()
	key_array = []
	key_index = 0
	cipher = []

	# create number array from key
	for i in range(len(key)):
		key_array.append(ord(key[i]) - 97)

	# apply cipher
	for i in range(len(plaintext)):

		# reset key back to beginning as needed
		if key_index >= len(key):
			key_index = 0

		# Add letters with shift to cipher array
		if plaintext[i].isalpha():
			if plaintext[i].isupper():
				cipher.append(chr((ord(plaintext[i]) - 65 + key_array[key_index])%26+65))
				key_index += 1
			else:
				cipher.append(chr((ord(plaintext[i]) - 97 + key_array[key_index])%26+97))
				key_index += 1
		else:
			cipher.append(plaintext[i])
			key_index += 1

	# make a string from cipher array
	ciphertext = ''.join(cipher)

	# print the cipher text
	print(ciphertext)

if __name__ == "__main__":
	main()
	exit(0)
	


