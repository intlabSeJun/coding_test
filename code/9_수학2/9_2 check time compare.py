"""
9_2 compare time with 1등
와 1등 에라스토체?? 이거 개빠르네 ㅋㅋㅋ
"""

total = 10000
random_ = 'off'

import time
import random


print('--mine--')
s = time.time()
list_num = list(range(1, total+1))
if random_ == 'on':
    random.shuffle(list_num)

count = 0
i=0
num = len(list_num)
decimal = []
while(num!=i):
    if list_num[i] >=10:
        break
    if list_num[i] in [2,3,5,7]:
        decimal.append(list_num[i])
        count += 1
    i+=1

if i != 0:
    del list_num[:i]

for n in list_num:
    last_num = n%10
    if last_num in [0, 2, 4, 6, 8]:
        continue
    else:
        a = int(n**(1/2)) # 제곱근
        for j in range(3, a+1,2):
            if n%j == 0:
                break
            elif j + 1 >= a:
                decimal.append(n)
                count += 1
if decimal == []:
    print(-1)
else:
    print(sum(decimal), decimal[0], sep='\n')
print(time.time() - s)



print('--1등--')
s = time.time()
arr = [False, False] + [True] * (total-1)
for i in range(2, 101):
    if arr[i]:
        for j in range(i * 2, len(arr), i):
            arr[j] = False

nums = [i for i in range(1, total+1) if arr[i]]
print(sum(nums)if len(nums) else -1)
print(min(nums) if len(nums) else '')
print(time.time() - s)