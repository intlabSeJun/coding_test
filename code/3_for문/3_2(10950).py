"""
단계 : 3-2
문제번호 : 10950번

문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다.
"""
case_count_T = int(input()) # 입력받을 줄 수
N = list(input() for _ in range(case_count_T)) # 줄 수에 따른 입력을 받고 리스트로 만들어줌.

for i in range(len(N)): # 받은 줄 수에 따라서 for문
    index = N[i].index(' ') # 문자열로 받아서 공백을 기준으로 인덱스 값 받아서
    sum = int(N[i][:index]) + int(N[i][index + 1:]) # 해당 인덱스를 기준으로 int로 바꾸어서 합산.
    print(sum)