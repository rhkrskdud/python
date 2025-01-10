a,b,c = map(int, input().split())

print(f"{(a+b)%c}")
print(f"{((a%c)+(b%c))%c}")
print(f"{(a*b)%c}")
print(f"{((a%c)*(b%c))%c}")