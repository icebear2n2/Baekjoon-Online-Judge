h, w, n = map(int, input().split())

if n - h > 0:
    num = n - (h * (n // h))
    num2 = (n // h) + 1
else:
    num = n - h
    num2  = n

print(num, 0, num2)