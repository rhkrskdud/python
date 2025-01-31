while(True):
    hap = 0
    n = int(input())
    if n == -1:
        break
    arr = [i for i in range(1,n) if n%i == 0]
    
    hap = sum(arr)
    
    if hap == n:
        print(f"{n} = ",end="")
        for i in arr[:-1]:
            print(f"{i} + ",end="")
        print(arr[-1])
    else:
        print(f"{n} is NOT perfect.")
        