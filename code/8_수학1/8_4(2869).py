import math
num = list(map(int, input().split()))
print(1 + math.ceil((num[2]-num[0])/(num[0]-num[1])))