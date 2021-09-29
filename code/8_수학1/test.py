
list = [1,2,3,4]

try:
    if any(list[i]>=5 for i in list):
        print(1)
except:
    print(222)