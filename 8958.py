import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    result = 0
    str = sys.stdin.readline().split('X')
    str = ' '.join(str).split()

    for i in range(0, len(str)):
        if len(str[i]) > 1:
            for j in range(1, len(str[i])+1):
                result += j
        else:
            result += 1
            
    print(result)