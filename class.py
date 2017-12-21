class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp1 = Employee('Nic', "Travis", 50000)
emp2 = Employee('Test', 'User', 40000)

# print(emp1)
# print(emp2)
Employee.fullname(emp1)
emp1.fullname()

# print(emp1.email)
# print(emp2.email)
print(emp1.fullname())
