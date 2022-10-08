lst = input()
lst = list(lst)

abc_list = []

for i in range(97, 123):
    abc_list.append(chr(i))

abc=' '.join(abc_list)

for i in range(len(lst)):
    if lst[i] in abc_list:
        abc=abc.replace(lst[i], str(lst.index(lst[i])))

for i in abc:
    if i in abc_list:
        abc=abc.replace(i, '-1')

print(abc)