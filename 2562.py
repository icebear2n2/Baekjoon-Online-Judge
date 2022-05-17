import sys

lst = []

for i in range(1, 10):
    A = int(sys.stdin.readline())
    lst.append(A)
    
print(sorted(lst)[-1])
print(lst.index(sorted(lst)[-1]) + 1)