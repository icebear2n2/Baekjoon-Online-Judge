A, B = map(str, input().split())
lst = []

A = int("".join(reversed(A)))
B = int("".join(reversed(B)))

lst.extend([A,B])

print(max(lst))