n =int(input())

for _ in range(n):
    i, s = input().split()
    i = int(i)
    
    for char in s:
        print(char*i,end="")
    print()