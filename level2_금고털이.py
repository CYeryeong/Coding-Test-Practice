import sys
 
input = sys.stdin.readline

w, n = map(int, input().split())
 
jewels = [list(map(int, input().split())) for _ in range(n)]
 
jewels.sort(key=lambda x: x[1], reverse=True)
 
answer = 0
for weight, price in jewels:
    if w > weight:
        answer += weight * price
        w -= weight
    else:
        answer += w * price
        break
 
print(answer)


#자꾸 시간초과된다. 왜?어떻게 고쳐야할까
#보석을 가방에 최대한 담되 가장 비싼 보석들을 위주로 가져가는 그리디 알고리즘 문제입니다.
#무게당 가격이 비싼 보석 순으로 가져가면 되며, 무게가 부족하면 톱으로 귀금속을 잘라서 
# 가져갈 수 있으므로 넣을 수 있는 무게만큼 최대한 가져가면 됩니다. 
# 보석을 가격순으로 정렬 후 반복하면서 (무게 * 무게 당 가격)만큼 answer를 증가시키고 
# 무게가 모자라면 (남은 공간 * 해당 보석의 무게 당 가격)을 증가시키고 반복을 멈추면 해결할 수 있습니다.


