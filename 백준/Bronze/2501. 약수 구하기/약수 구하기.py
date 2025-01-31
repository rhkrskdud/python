n,k = map(int, input().split())

#arr에 n의 약수들이 들어감!
arr =[i for i in range(1,n+1) if n%i == 0]

if k>len(arr):
    print(0)
else:
    print(arr[k-1])
