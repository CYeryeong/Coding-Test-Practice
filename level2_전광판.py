import sys
# 1 / 2 3 / 4 / 5 6 / 7 위에서부터
n_0 = [1, 1, 1, 0, 1, 1, 1]
n_1 = [0, 0, 1, 0, 0, 1, 0]
n_2 = [1, 0, 1, 1, 1, 0, 1]
n_3 = [1, 0, 1, 1, 0, 1, 1]
n_4 = [0, 1, 1, 1, 0, 1, 0]
n_5 = [1, 1, 0, 1, 0, 1, 1]
n_6 = [1, 1, 0, 1, 1, 1, 1]
n_7 = [1, 1, 1, 0, 0, 1, 0]
n_8 = [1, 1, 1, 1, 1, 1, 1]
n_9 = [1, 1, 1, 1, 0, 1, 1]
n_10n = [0, 0, 0, 0, 0, 0, 0]
n_list = [n_0, n_1, n_2, n_3, n_4, n_5, n_6, n_7, n_8, n_9, n_10n]
n = int(input())


for i in range(0,n):
    total = 0
    n1, n2= map(int, input().split())
    n1 = str('{0:05d}'.format(n1))
    n2 = str('{0:05d}'.format(n2))
    for z in (0,5):
        if n2[0:z+1] != 0*(z+1):
            for j in range(0,5):
                if n1[j] != n2[j]:
                    n1_num = n_list[int(n1[j])]
                    n2_num = n_list[int(n2[j])]
                    print(n1_num, n2_num)
                    for k in range(0,7):
                        if n1_num[k] != n2_num[k]:
                            total += 1
                        else :
                            continue
                else:
                    continue
        else : 
            n1_num = n_list[int(n1[j])]
            n2_num = n_list[10]
            for j in range(0,5):
                if n1[j] != n2[j]:
                    n1_num = n_list[int(n1[j])]
                    n2_num = n_list[int(n2[j])]
                    print(n1_num, n2_num)
                    for k in range(0,7):
                        if n1_num[k] != n2_num[k]:
                            total += 1
                        else :
                            continue
    print(total)


