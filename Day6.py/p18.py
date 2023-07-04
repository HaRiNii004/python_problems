#A website requires the users to input username and password to register. Write a program to check the validity of password input by users.


#Following are the criteria for checking the password:

#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12
#Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.


password =input("enter your password: ").split(',')
lst=[]
for x in password:
    if len(x)>= 6 and len(x)<=12:
            if any(y.isupper() for y in x)  and any(y.islower() for y in x) :
                    if any(y.isdigit for y in x) and (y in "@#$" for y in x): 
                            lst.append(x)

print(','.join(lst))