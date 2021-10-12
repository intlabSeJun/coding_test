"""
소수

문제
자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

입력
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

출력
M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.

단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.
"""

M = int(input())
N = int(input())

list_num = list(range(M, N+1))

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