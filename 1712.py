A, B, C = map(int, input().split())

i = 0
num1=0
num2=0
test1=(2100000000 * B) + A
test2=2100000000 * C

if test1 > test2:
    print(-1)
elif test1 == test2:
    i = 2100000001
    print(i)
    
else:
    while True:
        if num1 < num2:
            print(i)
            break
        
        i+=1
        num1=A+(B*i)
        num2=C*i
        