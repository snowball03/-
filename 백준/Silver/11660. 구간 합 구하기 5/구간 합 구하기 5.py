import sys
input = sys.stdin.read
data = input().split()

idx = 0
N, M = int(data[idx]), int(data[idx+1])
idx += 2

table = []
for _ in range(N):
    table.append(list(map(int, data[idx:idx+N])))
    idx += N

prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        prefix_sum[i][j] = (
            table[i-1][j-1] 
            + prefix_sum[i-1][j] 
            + prefix_sum[i][j-1] 
            - prefix_sum[i-1][j-1]
        )

results = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, data[idx:idx+4])
    idx += 4

    result = (
        prefix_sum[x2][y2]
        - prefix_sum[x1-1][y2]
        - prefix_sum[x2][y1-1]
        + prefix_sum[x1-1][y1-1]
    )
    results.append(result)

sys.stdout.write("\n".join(map(str, results)) + "\n")
