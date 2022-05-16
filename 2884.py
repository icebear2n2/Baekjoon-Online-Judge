H, M = map(int, input().split())
# 0 ≤ H ≤ 23, 0 ≤ M ≤ 59

if (H == 0 and M == 0) or (H == 0 and M < 45):
    H += 23
    M += 60
    M -= 45
    print(H,M)
elif H > 0:
    if M < 45:
        H -= 1
        M += 60
        M -= 45
        print(H, M)
    else:
        M-= 45
        print(H, M)
else:
    if M < 45:
        H += 23
        M += 60
        M -= 45
        print(H, M)
    else:
        M-= 45
        print(H, M)