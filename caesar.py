import sys

key = int(sys.argv[1])
plaintext = input("supply plaintext: ")
cipher = []
for i in range(len(plaintext)):
	if(plaintext[i].isalpha()):
		if(plaintext[i].isupper()):
			cipher.append(chr((ord(plaintext[i]) - 65 + key)%26+65))
		else:
			cipher.append(chr((ord(plaintext[i]) - 97 + key)%26+97))
	else:
		cipher.append(plaintext[i])

print(''.join(cipher))
