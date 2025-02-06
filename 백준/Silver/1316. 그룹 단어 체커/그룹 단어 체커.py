n = int(input())
count = 0

for _ in range(n):
    word = input()
    is_group_word = True
    for i in range(1, len(word)):
        if word[i] != word[i-1] and word[i] in word[:i]:
            is_group_word = False
            break
    if is_group_word:
        count += 1

print(count)
