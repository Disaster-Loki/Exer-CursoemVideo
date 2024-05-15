frase = str(input("Frase: ").upper().strip())
print("The letter A appeared: {}".format(frase.count('A')))
print("The first letter appeared in the position: {}".format(frase.find('A') + 1))
print("The last letter appeared  the position:  : {}".format(frase.rfind('A') + 1))
