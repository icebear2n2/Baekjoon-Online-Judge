import sys

N = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
average = 0
for i in lst:
    average+=i/lst[-1]*100

print(average/N)