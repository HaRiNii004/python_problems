'''Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
'''
tple=(1,2,3,4,5,6,7,8,9,10)
new_tuple=()
for i in tple:
    if i%2==0:
      new_tuple=list(new_tuple)  
      new_tuple.append(i)
      new_tuple=tuple(new_tuple)  

print(new_tuple)
print(type(new_tuple))
    