import sys

t = int(sys.stdin.readline().rstrip())

data = []
for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data.append(a + b)

count = 0
for i in data:
    count += 1
    print("Case #{}: {}".format(count, i))

