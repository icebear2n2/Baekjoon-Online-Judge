n, m = map(int, input().split())
lst = []
lst2 = []
for i in range(n+m):
    if i < n:
        lst += list(map(int, input().split()))
    else:
        lst2 += list(map(int, input().split()))
