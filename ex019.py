from random import choice
students = []
i = 1
while (i <= 4):
    students.append(str(input("{}ª student's name: ".format(i))))
    i += 2
print("Chosen student: {}".format(choice(students)))
