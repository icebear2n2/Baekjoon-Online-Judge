import sys

n = int(sys.stdin.readline())
count = 0

while True:
    if count == -1 or n == 0:
        break
    else:
        if n > 3:
            n -= 5
            if n < 0:
                count += -1
            else:
                count += 1
        else:
            n -= 3
            count += 1
            
            