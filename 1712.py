a, b, c = map(int, input().split())

num = c - b
try:
    num2 = a // num
except ZeroDivisionError:
    num2 = -1
    
if num2 < 0:
    print(-1)
else:
    print(num2+1)