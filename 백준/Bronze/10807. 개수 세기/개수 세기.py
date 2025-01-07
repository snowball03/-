a = int(input())
cnt = 0
num = []

num = list(map(int, input().split())) 

b = int(input())

for i in num:
    if b == i:
        cnt += 1 

print(cnt)

