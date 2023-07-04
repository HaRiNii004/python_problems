#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible
#by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

numbers = input("Enter the numbers: ").split(',')
lst = []

for x in numbers:
    number = int(x)  # Convert the string to an integer
    if len(x)!=4:
        continue
    if number % 5 == 0:
        lst.append(str(number))
        

print(",".join(lst))
