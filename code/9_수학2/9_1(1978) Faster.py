"""
소수 찾기

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
"""

num = int(input())
list_num = sorted(list(map(int, input().split())))
count = 0
i=0
while(num!=i):
    if list_num[i] >=10:
        break
    if list_num[i] in [2,3,5,7]:
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
                count += 1

print(count)
