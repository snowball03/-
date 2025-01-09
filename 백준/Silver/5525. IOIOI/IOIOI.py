n = int(input())
l = int(input())
s = input()
cnt = 0
j = 0

while j <= l - (2 * n + 1):
    match = True
    for k in range(2 * n + 1):
        if k % 2 == 0 and s[j + k] != 'I':
            match = False
            break
        elif k % 2 == 1 and s[j + k] != 'O':
            match = False
            break
    if match:
        cnt += 1
        j += 2  # 중복 방지
    else:
        j += 1

print(cnt)

