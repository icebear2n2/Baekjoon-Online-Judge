n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# B 리스트에 맞게 A 리스트를 제일 큰 수는 작은 걸로, 제일 작은 수는 큰 걸로 연결

a.sort()
b.sort(reverse=True)
temp = []
for i in range(n):
    temp.append(a[i] * b[i])

result = 0
for i in temp:
    result += i

print(result)