n1 = int(input())
n2 = input()

reverse_n2 = ''

for c in n2:
    reverse_n2 = c + reverse_n2

data_list = []
for c in reverse_n2:
    data_list.append(n1 * int(c))

data_list.append(n1 * int(n2))

for data in data_list:
    print(data)