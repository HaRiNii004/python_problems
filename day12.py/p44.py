'''Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
'''
lst=(range(1,21))
even_numbers=map(lambda i:i**2,lst)
print(list(even_numbers))