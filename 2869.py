A, B, V = map(int, input().split())
result = round(V / (A - B))

if result == V:
    print(result - B)
else:
    print(result)