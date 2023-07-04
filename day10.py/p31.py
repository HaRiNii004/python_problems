'''Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops'''
def dictionary():
    result = dict()
    for keys in range(1,21):
        values = keys**2
        result[keys]=values

    for key,value in result.items():
        print("{}:{}".format(key,value))
    
dictionary()
     