word = str(input("Word: "))
print("To Spaces: {}".format(word.isspace()) + "\n",
      "It's number: {}".format(word.isnumeric()) + "\n",
      "It's alphabetical: {}".format(word.isalpha()) + "\n",
      "It's alphanumeric: {}".format(word.isalnum()) + "\n",
      "It's in upper case: {}".format(word.isupper()) + "\n"
      "It's in lower case: {}".format(word.islower()) + "\n"
      "It's capitalized: {}".format(word.istitle()) + "\n"
      )