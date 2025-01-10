
a,b,c = map(int, input().split())

max = 0

if a==b and b==c:
    print(10000+a*1000)
elif a==b or b==c:
    print(1000+b*100)
elif a==c or b==c:
    print(1000+c*100)
else:
    if a>b:
        max = a
        if c>a:
            max = c
    else:
        max = b
        if c>b:
            max=c

    print(max*100)
    