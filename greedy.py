# Get input from the user
while True:
	print("Hi! How much change is owed: ", end="")
	c = float(input())*100
	if c > 0:
		break

# Variables
nickel = 5
dime = 10
quarter = 25
penny = 1

nickels = 0
dimes = 0
quarters = 0
pennies = 0
coins = 0

while c >= quarter:
	c -= quarter
	quarters += 1
	coins += 1

while c >= dime:
	c -= dime
	dimes += 1
	coins += 1

while c >= nickel:
	c -= nickel
	nickels += 1
	coins += 1

while c >= penny:
	c -= penny
	pennies += 1
	coins += 1


print("You will receive: \n{} quarter(s) \n{} dime(s) \n{} nickel(s) \n{} penny(pennies) \n{} coin(s) total".format(quarters, dimes, nickels, pennies, coins))


