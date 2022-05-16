import sys

n = int(sys.stdin.readline())
num = 0
tmp = -1
x = n // 10
y = n % 10

while True:
    if n == tmp:
        print(num)
        break
    else:
        num += 1
        tmp = (y * 10) + ((x + y) % 10)
        x = tmp // 10
        y = tmp % 10

