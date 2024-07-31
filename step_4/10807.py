n = int(input())
data = list(map(int, input().split()))
v = int(input())

count = 0
for i in data:
    if v == i:
        count += 1

print(count)