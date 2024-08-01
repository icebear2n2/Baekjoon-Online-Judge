str = input()
str_list = list(str)
reverse_str_list = list(reversed(str))

if str_list == reverse_str_list:
    print(1)
else:
    print(0)