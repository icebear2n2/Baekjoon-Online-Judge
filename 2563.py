n = int(input())
lst = []
for i in range(n):
    lst += [list(map(int, input().split()))]

num1 = 10 - (lst[2][0] - lst[0][0])
num2 = (lst[0][1] + 10) - (lst[0][1] - lst[2][1]) - lst[0][1]

print((100*n) - (num1*num2))