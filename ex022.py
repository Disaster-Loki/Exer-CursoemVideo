name = str(input("Full Name: ")).strip()
print("Name in Upper case: {}".format(name.upper()))
print("Name in Lower case: {}".format(name.lower()))
print("Letters: {}".format(len(name) - name.count(" ")))
print("First Name: {}".format(name.find(" ")))