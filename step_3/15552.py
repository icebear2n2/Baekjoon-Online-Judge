import sys
t = int(sys.stdin.readline().rstrip())

data = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    data.append(a + b)

for i in data:
    print(i)
