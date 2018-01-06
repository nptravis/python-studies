import sqlite3
from employee import Employee

# database that lives on disk:
# conn = sqlite3.connect('employee.db')

# database that lives in memory(on RAM):
conn = sqlite3.connect(':memory:')

c = conn.cursor()

# the quotes make a docstring, writes a string with multiple lines

# ran this once, which created the table, then comment it out to add data to the table to avoid 'table already exists' error, unless running in memory :)
c.execute("""CREATE TABLE employees (
					first text,
					last text,
					pay real
					)""")

def insert_emp(emp):
	# using context manager statement 'with' so will automatically commit after the insert
	with conn:
		c.execute("INSERT INTO employees VALUES(:first, :last, :last)", {'first': emp.first, 'last': emp.last,'pay': emp.pay,})

def get_emps_by_name(lastname):
	# don't need to commit a select statement, so no context manager
	c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
	return c.fetchall()

def update_pay(emp, pay):
	with conn:
		c.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last,'pay': emp.pay,})

def remove_emp(emp):
	with conn:
		c.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000.00)
emp_2 = Employee('Jayne', 'Doe', 1000000.00)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)


# c.execute("INSERT INTO employees VALUES('Mookie', 'Abrams-Travis', 00.00)")

# following string formating is bad! Leaves you vulnerable to SQL injection attacks!!!
# c.execute("INSERT INTO employees VALUES('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))

# # instead use ? placeholders
# c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_2.pay))
# # or colon placeholders
# c.execute("INSERT INTO employees VALUES(:first, :last, :last)", {'first': emp_2.first, 'last': emp_2.last,'pay': emp_2.pay,})

# here the comma at the end of the tuple is needed or else you'll get an error
# c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
# print(c.fetchall())

# c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Travis'})
# print(c.fetchall())

# print(c.fetchone())
# c.fetchmany(5)
# print(c.fetchall())

# conn.commit()

conn.close()