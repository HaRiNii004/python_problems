#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 _ C _ D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

import math
raw_input=input("number")
c = 50
h = 30
value = []
items = raw_input.split(',')
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print (','.join(value))