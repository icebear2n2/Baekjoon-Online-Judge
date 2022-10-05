ran = int(input())
result = 0

num = str(input())
lst = list(num)

for i in range(ran):
    result+=int(lst[i])
    
print(result)