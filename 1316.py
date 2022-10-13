count = 0

n = int(input())

for i in range(n):
    abc = str(input())
    tmp = []

    abc_lst = list(abc)
    set_lst = list(set(abc_lst))

    if len(abc_lst) == len(set_lst):
        count += 1
    else:
        for i in abc:
            if abc.count(i) >= 2:
                abc_index_list = list(filter(lambda x: abc[x] == i,range(len(abc))))
                for j in range(len(abc_index_list)):
                    if (j+1) == len(abc_index_list):
                        break
                    
                    tmp.append(abc_index_list[j+1] - abc_index_list[j])

        if len(list(set(tmp))) == 1 and list(set(tmp))[0] == 1:
            count += 1

print(count)