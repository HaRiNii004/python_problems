'''With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
'''
tple=(1,2,3,4,5,6,7,8,9,10)
for i in tple:
    first = (tple[:5])
    last =  (tple[-5:])
print(first)
print(last)
print(type(tple))
    