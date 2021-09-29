"""
N과 M (1)
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

"""
백트래킹(backtracking)이란? : 해를 찾는 도중 해가 아니어서 막히면, 되돌아가서 다시 해를 찾아가는 기법을 말합니다.
일반적으로, 불필요한 경로를 조기에 차단할 수 있게 되어 경우의 수가 줄어들지만, 
만약 N!의 경우의 수를 가진 문제에서 최악의 경우에는 여전히 지수함수 시간을 필요로 하므로 처리가 불가능 할 수도 있습니다.
가지치기를 얼마나 잘하느냐에 따라 효율성이 결정되게 됩니다.
"""
import math


def swap(sub_num, M):
    M = M
    global list_N, list_N_str
    index = -1

    if M-sub_num == -1:
        return
    change_index = M - sub_num-1
    for j in list_N[M-sub_num:]:
        if list_N[change_index] < j:
            index = list_N.index(j)
            break
    if index == -1:
        list_N[M-sub_num-1:] = sorted(list_N[M-sub_num-1:])

        swap(sub_num=sub_num+1, M=M)
    if index != -1:
        buf = list_N[change_index]
        list_N[change_index] = list_N[index]
        list_N[index] = buf
        list_N[M - sub_num:] = sorted(list_N[M - sub_num:])

        list_N_str = list(map(str,list_N))


N, M = list(map(int,input().split()))
list_N = list(range(1,N+1)) # 1~N까지 int 리스트로 저장. [,N]
list_N_str = list(map(str, list_N))#1~N까지 str 리스트로 저장. [,N]

for _ in range(math.factorial(N)//math.factorial(N-M+1)): # 계산을 통해 나온 반복 수
    print(" ".join(list_N_str[:M])) # int리스트는 바뀌는데 거기서 0~2번 index 값들만 출력
    for k in range(N-M):
        print(" ".join(list_N_str[:M-1] + list(list_N_str[M+k])))
    if M > 1:
        swap(1, M)
    else:
        break

