import sys

a = list(map(int, sys.stdin.readline().split()))

def solve(a):
    ans = 0
    for i in a:
        ans+=i
    return ans

