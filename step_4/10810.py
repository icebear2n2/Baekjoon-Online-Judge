n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(0)

for i in range(m):
    i, j, k = map(int, input().split())
    for j in range(i-1, j):
        data[j] = k

print(*data)