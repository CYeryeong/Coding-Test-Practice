import sys

Mon_in, Mon_out = input().split()
Tue_in, Tue_out = input().split()
Wen_in, Wen_out = input().split()
Thur_in, Thur_out = input().split()
Fri_in, Fri_out = input().split()

Time_list = [Mon_in, Mon_out, Tue_in, Tue_out, Wen_in, Wen_out, Thur_in, Thur_out, Fri_in, Fri_out]
Time = []
Work_Time = []
for i in Time_list :
    Time.extend(i.split(':'))

print(Time)
for i in range(0, 11) :
    if i%2 == 0 and int(Time[i+2]) - int(Time[i]) > 0:
        Work_Time.append(int(Time[i+2]) - int(Time[i]))
    elif i%2 == 0 and int(Time[i+2]) - int(Time[i]) < 0:
        Work_Time.append(- int(Time[i+2]) + int(Time[i]))
    elif i%2 != 0 and int(Time[i+2]) - int(Time[i]) < 0 :
        Work_Time.append(60 + Time[i+2]) - int(Time[i])
    else :
        Work_Time.append(int(Time[i+2]) - int(Time[i]))
print(Work_Time)
result = 0

for i in range(len(Work_Time)):
    if i%4 == 0:
        result = result + 60*Work_Time[i]
        print(result)
    else :
        result = result + Work_Time[i]
        print(result)

