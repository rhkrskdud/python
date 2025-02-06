n = int(input())

count = 0
#666부터 시작
num = 666

while(True):
    #숫자 666을 문자화 해서 문자화한 num안에 666이라는 글자가 있는지 확인..
    if '666' in str(num):
        count += 1
        if count  == n:
            print(num)
            break
    num += 1