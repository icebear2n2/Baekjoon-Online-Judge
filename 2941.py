dic = {'c=': 'č', 'c-': 'ć', 'dz=': 'dž', 'd-': 'đ', 'lj': 'lj', 'nj': 'nj', 's=': 'š', 'z=': 'ž'}
count = 0

n = str(input())

for key, value in dic.items():
    if key in n:
        while True:
            if key not in n:
                break
            else:
                n = n.replace(key, ' ', 1)
                count+=1

n = ' '.join(n).split()

print(len(n) + count)
            
        
        
