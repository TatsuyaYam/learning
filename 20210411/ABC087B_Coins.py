A = int(input())
B = int(input())
C = int(input())
X = int(input())

cntA = 0
ans = 0

while A >= cntA:
    cntB = 0
    while B >= cntB:
        cntC = 0
        while C >= cntC:
            if (500*cntA + 100*cntB + 50*cntC) == X:
                ans+=1
            cntC+=1
        cntB+=1
    cntA+=1

print(ans)