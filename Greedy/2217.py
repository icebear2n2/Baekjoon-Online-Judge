n = int(input())
data = []

for i in range(n):
    data.append(int(input()))

data.sort()

answer = []
for i in data:
    answer.append(i * n)
    n -= 1
    
print(max(answer))