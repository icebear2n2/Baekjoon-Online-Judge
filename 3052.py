import sys

lst = []

for i in range(1, 11):
    A = int(sys.stdin.readline())
    lst.append(A%42)

print(len(set(lst)))