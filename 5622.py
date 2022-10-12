num_dic = {2: ['A', 'B', 'C'], 3:['D', 'E', 'F'], 4:['G','H','I'], 5:['J','K','L'], 6:['M','N','O'], 7:['P', 'Q', 'R', 'S'], 8:['T', 'U', 'V'], 9:['W', 'X', 'Y', 'Z']}

n = str(input())
num_lst=[]
result=0

for key, value in num_dic.items():
    for i in n:
        if i in value:
            num_lst.append(key)

for i in num_lst:
    result+=(i+1)

print(result)