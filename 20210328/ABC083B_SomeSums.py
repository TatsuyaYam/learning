N,A,B = map(int,input().split())
ans = 0
tmp = 1
matchList = list()
while N >= tmp:
    ls = list(str(tmp))
    a = 0
    for i in ls:
        a += int(i)
    
    if (A <= a) and (B >= a):
        matchList.append(tmp)
    tmp += 1

for i in matchList:
    ans += int(i)

print(ans)