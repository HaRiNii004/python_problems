'''Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Use map() to generate a list.Use lambda to define anonymous functions.
'''
lst=(1,2,3,4,5,6,7,8,9,10)
square_root=map(lambda x:x**2,lst)
print(list(square_root))

'''Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
'''
lst=(1,2,3,4,5,6,7,8,9,10)
square_root=map(lambda x:x**2,lst)
even_numbers=filter(lambda x:x%2==0,square_root)
print(list(even_numbers))