table = [list(input().split()) for _ in range(5)]

data = ['' for i in range(15)]

for i in range(len(table)):
    for j in range(len(table[i])):
        for k in range(len(table[i][j])):
            data[k] += table[i][j][k]

result = ''
for i in data:
    result += i

print(result)