"""
소수 찾기

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
"""

import  time
s = time.time()
list_num = list(range(0,1000))

count = 0
for i in range(1000):
    last_num = list_num[i]%10
    if last_num in [0, 2, 4, 6, 8]:
        continue
    else:
        if list_num[i] < 10 and list_num[i] != 1 and list_num[i] != 9:
            print(list_num[i])
            count +=1
        else:
            a = int(list_num[i]**(1/2)) # 제곱근
            for j in range(3, a+1):
                if list_num[i]%j == 0:
                    break
                elif j == a:
                    print(list_num[i])
                    count += 1
print(count)
print(time.time() - s)


