name = str(input("Full Name: ")).strip()
print("Name in Upper case: {}".format(name.upper()))
print("Name in Lower case: {}".format(name.lower()))
print("Letters: {}".format(len(name) - name.count(" ")))
split_name = name.split()
print("First Name is {} and {} letters".format(split_name[0], len(split_name[0])))