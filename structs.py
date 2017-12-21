import sys
import csv
from student import Student

students = []
for i in range(3):

	print("name: ", end="")
	name = input()

	print("dorm: ", end="")
	dorm = input()

	students.append(Student(name,dorm)) # similar to malloc
## this will print to the screen
# for student in students:
# 	print("{} is in {}.".format(student.name, student.dorm))

# this will save to a csv file
file = open("students.csv", "w")
writer = csv.writer(file)
for student in students:
	writer.writerow((student.name, student.dorm))
file.close()