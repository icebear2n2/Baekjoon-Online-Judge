data = [1, 1, 2, 2, 2, 8]

data2 = list(map(int, input().split()))

result = []
for i in range(len(data)):
    result.append(data[i] - data2[i])

print(*result)