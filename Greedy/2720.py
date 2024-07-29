n = int(input())
coin_list = [25, 10, 5, 1]
data_list = []

for _ in range(n):
    data_list.append(int(input()))

for data in data_list:
    result = []
    for coin in coin_list:
        count = 0
        
        count += int(data // coin)
        data = data % coin
        
        result.append(count)
    print(*result)
