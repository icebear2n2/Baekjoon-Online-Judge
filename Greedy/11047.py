n, k = map(int, input().split())

coin_list = []

for _ in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse=True)

count = 0
for i in range(n):
    count += k // coin_list[i] # 카운트 값에 K를 동전으로 나눈 몫을 더해준다.
    k = k % coin_list[i] # k는 동전으로 나눈 나머지로 계속 반복된다.

print(count)