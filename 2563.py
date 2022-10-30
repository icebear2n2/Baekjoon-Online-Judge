n = int(input())

x_list = []
y_list = []
xy_list = []
xy = 1

for i in range(n):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

for i in range(n-1):
    if (x_list[0] + 10) < x_list[i+1]:
        del x_list[i+1]
        
    elif (y_list[0] + 10) < y_list[i+1]:
        del y_list[i+1]

xy_list.append(list(set(x_list)))
xy_list.append(list(set(y_list)))

for i in range(len(xy_list)):
    xy *= 10 - (xy_list[i][-1] - xy_list[i][0])

result = (100 * n) - xy

print(result)
