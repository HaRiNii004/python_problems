#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

lines = input("type something: ")
lowercase=[]
uppercase=[]

for x in lines:
    if x.isupper():
        uppercase.append(x)
    if x.islower():
        lowercase.append(x)
        
print("uppercase:")
print(len(uppercase))
print("lowercase:")
print(len(lowercase))