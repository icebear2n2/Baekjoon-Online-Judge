str = input().upper()
set_str = list(set(str))

count = []
for i in set_str:
    count.append(str.count(i))

if count.count(max(count)) > 1:
    print("?")
else:
    print(set_str[(count.index(max(count)))])

