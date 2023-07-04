

a = input("enter a list of numbers: ").split(',')
lst=[]
for i in a:
    x = int(i)
    if x%2 != 0:
        lst.append(str(x*x))
print(','.join(lst))