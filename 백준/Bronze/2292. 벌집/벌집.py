n = int(input())

start = 6
count = 1

if n==1:
    print("1")
else:
    while n>1:
        n = n -(start*count)
        count += 1
    print(count)
    
    

