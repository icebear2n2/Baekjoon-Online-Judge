import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    lst = list(map(int, sys.stdin.readline().split()))
    num = lst.pop(0)
    num2 = 0
    
    for i in lst:
        if i > (sum(lst) / num):
            num2 += 1
        else:
            continue
    
    print("{:.3f}%".format(num2 / num * 100))