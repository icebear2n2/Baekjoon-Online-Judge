n, x = map(int, input().split())
a = list(map(int, input().split()))

result = []
for i in a:
    if i >= x:
        continue
    else:
        result.append(i)

print(*result)