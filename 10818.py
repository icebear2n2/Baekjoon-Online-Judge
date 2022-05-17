import sys

n = int(sys.stdin.readline())

lst = sorted(list(map(int, sys.stdin.readline().split())))
print(lst[0], end=' ')
print(lst[-1])