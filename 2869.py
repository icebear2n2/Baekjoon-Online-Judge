A, B, V = map(int, input().split())


if round(V / A) * A > V:
    print(round(V / A) + 1)
elif (A - B) == 1:
    print(V - B)
else:
    print(round(V / A) + 1)