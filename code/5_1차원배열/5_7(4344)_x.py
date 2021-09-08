"""
단계 : 5-7
문제번호 : 4344

문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
"""
import sys
case = int(input())
percent = []
for i in range(case):
    line = list(map(int, sys.stdin.readline().split())) # 받은 line을 공백 단위로 split해서 list 형태로 저장. + int형태로 전환.
    mean_line = sum(line[1:])/line[0]
    new_line = sorted(line[1:])
    for j, value in enumerate(new_line):
        if value > mean_line:
            percent.append((len(new_line)-j)/len(new_line))
            break

for k in range(len(percent)):
    print('%.3f%%' % (percent[k]*100))#"""


import sys
case = int(input())
percent = [0.000] * case
for i in range(case):
    line = list(map(int, sys.stdin.readline().split())) # 받은 line을 공백 단위로 split해서 list 형태로 저장. + int형태로 전환.
    mean_line = sum(line[1:])/line[0]
    new_line = sorted(line[1:])
    for j, value in enumerate(new_line):
        if value > mean_line:
            percent[i] = ((len(new_line)-j)/len(new_line))
            break

for k in range(len(percent)):
    print('%.3f%%' % (percent[k]*100))


