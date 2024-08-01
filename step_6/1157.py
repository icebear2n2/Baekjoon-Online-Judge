str = input()
str_list = list(str.lower())
set_str_list = set(list(str.lower()))

count = []
for i in set_str_list:
    count.append(str_list.count(i))