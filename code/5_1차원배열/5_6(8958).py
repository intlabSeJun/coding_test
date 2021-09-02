"""
단계 : 5-2
문제번호 : 8958

문제
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는
그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
문자열은 O와 X만으로 이루어져 있다.

출력
각 테스트 케이스마다 점수를 출력한다.
"""

"""
'X'에 해당하는 index만 받아서 피보나치로 합 구해줌, 그리고 해당 인덱스를 포함하여 이전 값들은 없애줌
ex) OOXOO -> X 인덱스 구하고 피보나치 계산하고, OO 로 만들어줌. 'X' 존재 하지 않을시 'O'의 수만큼 피보나치.
"""
case = int(input())
list_sum = []

# 피보나치 구함. 숫자 받아서 홀수/짝수 경우로 나누어서 구해서 반환.
# ex) num=3 : 1 2 3 이므로 (1+3)*1 + 2
#     num=4 : 1 2 3 4 이므로 (1+4)*2
def fibonacci(num):
    if num == 1:
        return num
    if num%2 != 0:
        value = (1 + num) * int(num/2) + (1 + num)/2
    else:
        value = (1 + num) * num/2

    return value


for i in range(case):
    o_x = input()
    num_x = o_x.count('X')

    sum = 0
    for j in range(num_x + 1):
        index = o_x.find('X') # find는 없을시에 -1 반환 / index는 없을시에 error뜸.
        if index == -1:
            sum += fibonacci(o_x.count('O'))
            break
        sum += fibonacci(index)
        o_x = o_x[index+1:]
    list_sum.append(int(sum))

for i in range(case):
    print(list_sum[i])