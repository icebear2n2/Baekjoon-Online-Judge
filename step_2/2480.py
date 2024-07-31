data = list(map(int, input().split()))
set_data = list(set(data))


if len(set_data) == 3:
    print(set_data[-1] * 100)
else:
    for i in set_data:
        count = data.count(i)

        if count == 3:
            print(10000 + i  * 1000)
        elif count == 2:
            print(1000 + i * 100)
        else:
            continue
    