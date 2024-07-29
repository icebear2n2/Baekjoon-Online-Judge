n = 1000 - int(input())
coin_list = [500, 100, 50, 10, 5, 1]
count = 0

for coin in coin_list:
    count += int(n // coin)
    n = n % coin

print(count)