import math
opposite = float(input("Length of opposite: "))
adjacent = float(input("Length of adjacent: "))
hypotenuse = math.sqrt(math.pow(opposite, 2) + math.pow(adjacent, 2))
print("Length of hypotenuse: {:.2f}".format(hypotenuse))