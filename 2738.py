n, m = map(int, input().split())
lst = []

for i in range(n+n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    lst2 = [lst[i][j] + lst[i+n][j] for j in range(m)]
    print(" ".join(map(str, lst2)))