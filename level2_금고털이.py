import sys

rest_g, n = map(int, input().split())
total_price = 0
Weight, price = [],[]

#lst 완성
for _ in range(n):
    Wei, pri = map(int, input().split())
    Weight.append(Wei)
    #Weight = [90,70]
    price.append(pri)
    #price = [1, 2]

while rest_g > 0 :
    max_g = Weight[price.index(max(price))]
    max_p = max(price)

    if max_g > rest_g :
        total_price += rest_g*max_p
        rest_g = 0

    else :
        total_price += max_g*max_p
        rest_g = rest_g - max_g
        Weight[price.index(max(price))] = 0
        price[price.index(max(price))] = 0 

print(total_price)

#자꾸 시간초과된다. 왜?어떻게 고쳐야할까



