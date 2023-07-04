'''Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
Hints:
Use len() function to get the length of a string.'''

str1 = input("enter string1: ")
str2 = input("enter string2: ")

def string_length(str1,str2):
    if len(str1)<len(str2):
        return(str2)
    elif len(str1)>len(str2):
        return(str1)
    else:
        return(str1)
        return(str2)
        
print(string_length(str1,str2))