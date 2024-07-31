n, m = map(int, input().split())

data = []
for i in range(1, n+1):
    data.append(i)


for x in range(m):
    temp = []
    i, j = map(int, input().split())
    temp.append(data[i-1])
    temp.append(data[j-1])
    data[i-1] = temp[-1]
    data[j-1] = temp[0]

print(*data)

