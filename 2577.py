import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

lst = []

for i in str( A*B*C):
    lst.append(int(i))
    
for j in range(0, 10):
    print(lst.count(j))