"""
9_1(1978) 주어진 수들 중에 소수를 구하는 문제에서
정렬되었다고 가정한다면, ( random으로 섞어도 동일 )
1등 코드가 가장 느리고, check2 코드가 가장 빠르다.( 10000개 이상부터)

* 아마 1등 코드가 제출시에 빠르게 나온 것은 파이썬 버전 때문이라고 생각됨.
"""

total = 1000
random_ = 'on'

import time
import random

print('--1등--')
s = time.time()
li=list(range(1,total))
if random_ == 'on':
    random.shuffle(li)
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)
print(time.time() - s)


print('--check1--')
s = time.time()
list_num = list(range(1,total))
if random_ == 'on':
    random.shuffle(list_num)
count = 0
for i in range(total-1):
    last_num = list_num[i]%10
    if last_num in [0, 2, 4, 6, 8]:
        continue
    else:
        if list_num[i] < 10 and list_num[i] != 1 and list_num[i] != 9:
            count +=1
        else:
            a = int(list_num[i]**(1/2)) # 제곱근
            for j in range(3, a+1):
                if list_num[i]%j == 0:
                    break
                elif j == a:
                    count += 1
print(count)
print(time.time() - s)

print('--check2--')
s = time.time()
list_num = list(range(1,total))
if random_ == 'on':
    random.shuffle(list_num)

count = 0
i=0
while(1):
    if list_num[i] >=10:
        break
    if list_num[i] in [2,3,5,7]:
        count += 1
    i+=1

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
            elif j+1 >= a:
                count+=1

print(count)
print(time.time() - s)