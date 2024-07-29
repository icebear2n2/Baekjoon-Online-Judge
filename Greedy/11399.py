n = int(input())
# 3 1 4 3 2
data = list(map(int, input().split()))

# 1 2 3 3 4
data.sort()

result = 0

for i in range(n+1):
    for j in range(i):
        result += data[j]
  
print(result)        
