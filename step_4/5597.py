data = []
for i in range(28):
    data.append(int(input()))

result = []
for i in range(1, 31):
    if i not in data:
        result.append(i)

print(*result)