'''Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.'''

def square_root():
    lst=list()
    for i in range(1,21):
        j=i**2
        lst.append(j)
    print(lst)
    
square_root()

'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the first 5 elements in the list.'''
def square_root():
    lst=list()
    for i in range(1,21):
        j=i**2
        lst.append(j)
    
    print(lst[:5])
    
square_root()

'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print the last 5 elements in the list.'''
def square_root():
    lst=list()
    for i in range(1,21):
        j=i**2
        lst.append(j)
    
    print(lst[-5:])
    
square_root()

'''Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
Then the function needs to print all values except the first 5 elements in the list.
'''
def square_root():
    lst=list()
    for i in range(1,21):
        j=i**2
        lst.append(j)
    
    print(lst[5:20])#print(lst[5:])

    
square_root()