n, m = map(int, input().split())
lst = []
lst2 = []
for i in range(n+m):
    if i < n:
        lst += [list(map(int, input().split()))]
    else:
        lst2 += [list(map(int, input().split()))]

for i in range(len(lst)):
    c = [lst[i][j] + lst2[i][j] for j in range(len(lst))]
    for i in c:
        print(i, end=' ')
    print()