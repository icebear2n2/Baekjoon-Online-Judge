n = int(input())

lst = []
lst2 = []
for i in range(n):
    num1, num2 = map(int, input().split())
    lst.append(num1)
    lst2.append(num2)

lst.sort()
lst2.sort()

num1 = (lst[-1] - lst[1]) - (lst[1] - lst[0])
num2 = lst2[-1] - lst2[0]

print((100 * n) - (num1*num2))