n,s,d = map(int,input().split())
cnt = 0

while cnt < n:
    x,y = map(int,input().split())
    if s > x and d < y:
        break
    cnt = cnt + 1

if cnt < n:
    print('Yes')
else:
    print('No')

#回答例
N, S, D = map(int, input().split())
def check():
    X, Y = map(int, input().split())
    return X < S and Y > D

if any(check() for i in range(N)):
    print("Yes")
else:
    print("No")

