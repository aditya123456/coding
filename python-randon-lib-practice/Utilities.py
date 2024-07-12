


list = [1, 4, 5, 6, 0, 4]
print(any(list))
print(all(list))

with open("file.txt") as fp:
    for i in iter(fp.readline, ''):
        print(i)

for k , v in enumerate(list):
    print(k, v)



def filterfunction1(c):
    pass

def filterfunction2(x):
    pass

def squar(x):
    pass


odd = list(filter(filterfunction2, list))

squar1 = list(map(squar, list))


import itertools

list2 = ["name1", "aditya", "amit", "sdfdfd"]

print(itertools.count(list2))