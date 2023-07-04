x=int(input("enter value for rows"))
y=int(input("enter value for columns"))
lst=[]
temp=[]
for i in range(x):
 temp=[]
 for j in range(y):
  temp.append(i*j)
  lst.append(temp)   
print(lst)
