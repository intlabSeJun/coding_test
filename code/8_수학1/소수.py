
a,b = list(map(int,input().split()))
abc = list(range(a,b+1))

for n in [2,3,5,7]:
    abc = list(filter(lambda x: x%n!=0, abc))


for i in abc:
    print(i)#"""


