b = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()

for i in b:
    str = str.replace(i, '*')

print(len(str))