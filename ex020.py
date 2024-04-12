import random
students = []
i = 1
while (i <= 4):
    students.append(str(input("{}ª student's name: ".format(i))))
    i += 1
random.shuffle(students)
print("Presentation order: {}".format(students))