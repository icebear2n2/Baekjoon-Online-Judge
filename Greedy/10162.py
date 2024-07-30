n = int(input())
time_list = [300, 60, 10]

result = []
for time in time_list:
    result.append(n // time)
    n = n % time

if n != 0:
    print(-1)
else:
    print(*result)