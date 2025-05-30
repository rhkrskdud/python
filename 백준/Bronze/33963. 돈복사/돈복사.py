def cal(money, 자리수):
    while True:
        if money // 10 == 0:
            자리수 = 자리수 + 1
            return 자리수
        else:
            money = money // 10
            자리수 = 자리수 + 1


money = int(input())
time = 0
리얼자리수 = 0
가짜자리수 = 0

리얼자리수 = cal(money, 리얼자리수)

while True:
    가짜자리수 = 0
    가짜자리수 = cal(money, 가짜자리수)
    if 리얼자리수 != 가짜자리수:
        time = time - 1
        break
    else:
        money = money * 2
        time = time + 1

print(time)