import sys
input = sys.stdin.read

data = input().split()
numCnt, sumCnt = int(data[0]), int(data[1])
num = list(map(int, data[2:numCnt+2]))

prefix_sum = [0] * (numCnt + 1)
for i in range(1, numCnt + 1):
    prefix_sum[i] = prefix_sum[i-1] + num[i-1]

queries = data[numCnt+2:]
results = []
for i in range(sumCnt):
    f, l = int(queries[i*2]), int(queries[i*2+1])
    results.append(prefix_sum[l] - prefix_sum[f-1])

sys.stdout.write("\n".join(map(str, results)) + "\n")
# 입력과 출력 모두 sys.stdin과 sys.stdout을 사용하여 속도를 최적화.

        