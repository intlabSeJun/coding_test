"""
단계 : 6-3
문제번호 : 1065

문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""
def count_x(num):
    y = 0
    for i in range(1, num):
        y += (10 - i) // 2 + i // 2 + 1
        if i%2 == 0:
            y -= 1
    return 99 + y

n_list = list(map(int,list(input())))
num = n_list[0]
count = 0

if len(n_list) == 1:
    count = int(str(n_list[0]))
elif len(n_list) == 2:
    count = int(str(n_list[0]) + str(n_list[1]))
elif len(n_list) == 4:
    count = count_x(10)
else:
    count = count_x(num)
    total_num = int(str(n_list[0]) + str(n_list[1]) + str(n_list[1]))
    if num < n_list[1]:
        n = (10 - num) // 2
        if num%2 == 0:
            n -= 1
        for j in range(1,n+1):
            b = n_list[1] - num
            if b == j and n_list[1]>=(n_list[1] + j):
                count += 1
    else:
        n = num // 2
        for k in range(n+1):

            if (num-n_list[1]) == k and (n_list[1]-n_list[2])==k:
                count += 1
print(count)