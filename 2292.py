n = int(input())

count = 2
num = 6
result = 7

while True:
    if n == 1:
        print(1)
        break
    elif n <= result:
        print(count)
        break
    else:
        count += 1
        num += 6
        result+=num