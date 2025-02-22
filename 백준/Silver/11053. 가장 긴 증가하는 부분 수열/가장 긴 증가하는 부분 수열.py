def lis(a):
    n = len(a)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)


n = int(input())
arr = list(map(int, input().split()))

print(lis(arr))