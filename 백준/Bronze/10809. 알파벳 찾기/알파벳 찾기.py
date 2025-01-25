arr = [-1] *26

s =input()
num=0
for i in s:
    if arr[ord(i)-ord('a')] == -1:
        arr[ord(i)-ord('a')] = num
    num += 1
    
print(*arr)