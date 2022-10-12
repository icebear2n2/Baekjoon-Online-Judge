n = str(input())
n = n.upper()
num_lst = []

set_n = list(set(n))

for i in set_n:
    num_lst.append(n.count(i))

max_num = max(num_lst)

if num_lst.count(max_num) >= 2:
    print('?')
else:
    print(set_n[num_lst.index(max_num)])
