 # Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a 
 # single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320
 
 
n=int(input("enter any number: "))
fact=1
i=1
while i<=n:
 fact=fact*i
 i+=1
print(fact)