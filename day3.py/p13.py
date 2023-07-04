#Write a program that accepts a sentence and calculate the number of letters and digits.

lines = input("type something: ")
letters=[]
numbers=[]
for i in lines:
    if i.isdigit():
        numbers.append(i)
    elif i.isalpha:
        letters.append(i)
    
 
print("letters: ")
print(len(letters))
print("numbers: ")
print(len(numbers))   
