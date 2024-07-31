n, m = map(int, input().split())
data = []
for i in range(1, n+1):
    data.append(i)

for x in range(m):
    i, j = map(int, input().split())
    temp = data[i-1:j]
    temp.reverse()

    data[i-1:j] = temp

print(*data)