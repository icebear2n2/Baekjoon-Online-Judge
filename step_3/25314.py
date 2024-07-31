n = int(input())

data = []
for i in range(n // 4):
    data.append("long")

print(*data, "int")