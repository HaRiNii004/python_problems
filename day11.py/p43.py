'''Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
'''
lst=(range(0,21))
even_numbers=filter(lambda i:i%2==0,lst)
print(list(even_numbers))