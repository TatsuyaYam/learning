N = int(input())
a = list(map(int,input().split()))
alice = list()
bob = list()
switch = 0

while len(a) > 0:
    b = max(a)
    idx = a.index(b)
    if switch == 0:
        alice.append(b)
        switch = 1
    else:
        bob.append(b)
        switch = 0
    del a[idx]

asum = 0
for i in alice:
    asum += int(i)
bsum = 0
for i in bob:
    bsum += int(i)

print(asum - bsum)