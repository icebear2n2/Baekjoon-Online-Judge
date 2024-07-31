n = int(input())
data = list(map(int, input().split()))
max_score = max(data)

result = []
for i in data:
    result.append(i / max_score * 100)

avg = 0
for i in result:
    avg += i

print(avg / n)