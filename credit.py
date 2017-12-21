
cc = input("Enter credit card number: ")

def main():
	if(cc == None):
		print("Error with input")
	elif (cc.isnumeric() != True):
		print("Error, numbers only")
	elif (len(cc) != 16) and (len(cc) != 13) and (len(cc) != 15) or (cc.isnumeric() != True):
		print("Invalid Number")
	else:
		if numTest():
			if cardType() == 1:
				print("AMEX")
			elif cardType() == 2:
				print("MasterCard")
			elif cardType() == 3:
				print("Visa")
			else:
				print("Error")
		else:
			print("Error with num test")

def cardType():
	if len(cc) == 15:
		temp1 = cc[0] + cc[1]
		if (int(temp1) == 34) or (int(temp1) == 37):
			return 1
	elif (len(cc) == 16) and (int(cc[0]) !=4):
		temp1 = cc[0] + cc[1]
		if int(temp1) >= 51 and int(temp1) <= 55:
			return 2
	elif len(cc) == 13 or len(cc) == 16:
		if int(cc[0]) == 4:
			return 3
	else:
		return 4

def numTest():
	total = 0
	for i in range(len(cc)-2,len(cc), -2):
		if (int(cc[i])*2) >= 10:
			temp = str(int(cc[i])*2)
			total += (int(temp[0]) + int(temp[1]))
		else:
			total += int(cc[i])*2

	for i in range(len(cc)-1, len(cc), -2):
		total += int(cc[i])

	if (total%10) == 0:
		return True

	else:
		return False



if __name__ == "__main__":
	main()

