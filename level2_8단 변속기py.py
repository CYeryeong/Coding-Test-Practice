import sys
input_lst = list(map(int, sys.stdin.readline().split()))
# 이게 중요하다!! 메모리를 많이 차지ㅇ하지 않는다
result = 0

for i in range(7):
    if input_lst[i+1] == input_lst[i]+1:
        result +=1
    elif input_lst[i+1] == input_lst[i]-1:
        result -= 1

if result == 7:
    print('ascending')
elif result == -7 :
    print('descending')
else:
    print('mixed')

