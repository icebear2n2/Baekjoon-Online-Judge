A, B, C = map(int, input().split())
result = 0

if (A == B) and (B == C) and (A == C):
   result = 10000 + (A * 1000)
elif (A == B) and (A != C):
    result = 1000 + (A * 100)
elif  (A == C) and (A != B):
    result = 1000 + (A * 100)
elif (B == C) and (B != A):
    result = 1000 + (B * 100)
else:
    if A > B and A > C:
        result = A * 100
    elif B > A and B > C:
        result = B * 100
    elif C > A and C > B:
        result = C * 100
    else:
        print('error')
        
print(result)


