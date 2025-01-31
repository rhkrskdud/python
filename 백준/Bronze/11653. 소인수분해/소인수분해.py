n = int(input())
if n == 1:
    print("")
else:
    while n != 1:
        # print("wait~ ")
        for i in range(2, n + 1):
            # print("what?")
            if n % i == 0:
                print(i)
                n = n // i
                break
