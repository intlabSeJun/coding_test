"""
단계 : 6-3
문제번호 : 1065

문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
"""



n_list = list(map(int,list(input())))

length= len(n_list)
total_num = 0
for i in range(1,length+1):
    total_num += n_list[-i]*10**(i-1)

hundred_x = n_list[0]
total_count = 0

if length <= 2 :
    total_count = total_num
elif length == 4:
    total_count = 99 + 9*5
else:
    total_count = 99 + (hundred_x-1)*5
    if n_list[0] < n_list[1]:
        for i in range(1, (9-hundred_x)//2 + 1):
            num = hundred_x*100 + (hundred_x+i)*10 + hundred_x+2*i
            if num <= total_num:
                total_count +=1
            else:
                break
        total_count += hundred_x // 2 + 1
    else:
        for i in range(0, hundred_x//2+1):
            num = hundred_x*100 + (hundred_x-i)*10 + hundred_x-2*i
            if num <= total_num:
                total_count += hundred_x//2 +1 - i
                break
print(total_count)
