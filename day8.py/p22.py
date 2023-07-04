#Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

data = input ( "enter the sentence: ").split(" ")
empty = {}
for x in data:
    cnt= data.count(x)
    empty[x]=cnt

sorted_list=sorted(empty.keys())
for keys in sorted_list:
    print("{}:{}".format(keys, cnt))