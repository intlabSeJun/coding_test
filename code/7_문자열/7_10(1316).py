"""
문제
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

출력
첫째 줄에 그룹 단어의 개수를 출력한다.
"""

"""
알고리즘 풀이
: 문자열을 받아서 첫번쨰 문자열부터 중복되는 문자열을 찾고 해당 문자열의 개수를 받아서, 개수만큼 슬라이싱을 통해 처음 받은 문자열을 set 함수
사용하여 종류를 받아냄. 종류가 1개 또는 종류게 해당하는 문자열이 아니면 break, 이러한 과정을 모두 거처 break가 일어나지 않으면 그룹이라고
판정. 
"""
#"""
n = int(input())

count =0
for i in range(n):
    string = list(input())

    for j,k in enumerate(string):
        if j == len(string) - 1:

            count += 1
            break
        if k in string[j+1:]:
            a = string[j+1:].count(k)
            st2 = list(set(string[j+1:j+1+a]))

            if len(st2) != 1 or st2[0] != k:

                break
        else:
            continue

print(count)
#"""


# 1등 코드
result = 0
for i in range(int(input())):
    word = input()
    print(sorted(word, key=word.find)) # key=word.find 는 기존 순서는 유지한체 정렬.
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)