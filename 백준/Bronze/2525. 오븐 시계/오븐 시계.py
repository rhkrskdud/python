h, m = map(int, input().split())
mm = int(input())

if m + mm < 60:
    print(h, m + mm)
elif m + mm >= 60:
    if h + ((m + mm) // 60) < 24:
        print(h + ((m + mm) // 60), (m + mm) % 60)
    elif h + ((m + mm) // 60) >= 24:
        print((h + ((m + mm) // 60)) - 24, (m + mm) % 60)
