'''Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
'''

import math
def square_root(x):
    '''
    the given function returns the square root of the variable x
    '''
    return math.sqrt(x)
    
print("documentation for abs:")
print(abs.__doc__)

print("\ndocumentation for int: ")
print(input.__doc__)

print("\ndocumentation for input(): ")
print(int.__doc__)

print("\ndocumentation for square_root()")
print(square_root.__doc__)