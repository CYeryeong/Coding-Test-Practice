import sys

Mon_in, Mon_out = input().split()
Tue_in, Tue_out = input().split()
Wen_in, Wen_out = input().split()
Thur_in, Thur_out = input().split()
Fri_in, Fri_out = input().split()

Time_list = [Mon_in, Mon_out, Tue_in, Tue_out, Wen_in, Wen_out, Thur_in, Thur_out, Fri_in, Fri_out]
Time, Work_Time_Hours, Work_Time_Min = [], [], []
result= 0 

for i in Time_list :
    Time.extend(map(int, i.split(':')))

# Time = [10, 0, 19, 0, 9, 0, 15, 0, 10, 0, 11, 0, 11, 0, 22, 0, 9, 0, 15, 0]
# 2-0 = Mon_hour, 3-1 = Mon_min => 4를 한 턴으로
# hour은 음수일리 없음, min의 경우 음수이면 +60 하면 됨 그럴 경우에는 hour-60도 필요
for i in range(len(Time)//4):
    Work_Time_Hours.append(60*(Time[i*4+2] - Time[i*4]))
    if Time[i*4+3] - Time[i*4+1] < 0:
        Work_Time_Min.append(60+Time[i*4+3] - Time[i*4+1])
        Work_Time_Hours[i] -= 60
    else:
        Work_Time_Min.append(Time[i*4+3] - Time[i*4+1])

total = Work_Time_Hours + Work_Time_Min
for i in range(len(total)):
    result += total[i]

print(result)
