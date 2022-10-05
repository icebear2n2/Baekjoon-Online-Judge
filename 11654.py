n = input()

if type(n) == type('A'):
    print(ord(n))
else:
    print(chr(n))