s = input().lower()

arr = [0] * 26

for i in s:
    arr[ord(i) - ord('a')] = arr[ord(i) - ord('a')] + 1

max = max(arr)

sibal = [i for i in range(26) if arr[i] == max]

if len(sibal) > 1:
    print('?')
else:
    print(chr(sibal[0] + ord('A')))