while(True):
    arr = list(map(int, input().split()))
    
    if arr == [0,0,0]:
        break
        
    max_len = max(arr)
    
    if max_len >= (sum(arr) - max_len):
        print("Invalid")
    else:
        if arr[0] == arr[1] == arr[2]:
            print("Equilateral")
        elif arr[0] != arr[1] and arr[0] != arr[2] and arr[1] != arr[2]:
            print("Scalene")
        else:
            print("Isosceles")