'''Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
'''
def square_root():
    tple=tuple()
    for i in range(1,21):
        j=i**2
        tple=list(tple)
        tple.append(j)
        tple=tuple(tple)
    print(tple)
    print(type(tple))
square_root()