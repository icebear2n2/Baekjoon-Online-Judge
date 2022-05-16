import sys

N = int(sys.stdin.readline())
num = 1

for i in range(N-1, -1, -1):
    print("{0}{1}".format(chr(32)*i, chr(42)*num))
    num +=1