name = str(input("Name: ")).strip()
print("Nice to meet you !!")
name = name.split()
print("First Name: {}".format(name[0]))
print("Last Name: {}".format(name[len(name)-1]))