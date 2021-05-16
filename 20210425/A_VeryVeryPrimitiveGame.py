a,b,c = map(int,input().split())

if c == 0:
    if b >= a:
        print('Aoki')
    else:
        print('Takahashi')
else:
    if a >= b:
        print('Takahashi')
    else:
        print('Aoki')

#回答例
A, B, C = map(int, input().split())
if A + C > B:
    print("Takahashi")
else:
    print("Aoki")

