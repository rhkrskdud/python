a, b = input().split()

a = a[-1] + a[1] + a[0]
b = b[-1] + b[1] + b[0]

if int(a)>int(b):
    print(int(a))
else:
    print(int(b))
