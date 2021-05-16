import itertools

l1 = list(map(int,input().split()))
l1.sort(reverse=True)

ans1 = l1[0] - l1[1]
ans2 = l1[1] - l1[2]

if ans1==ans2:
    print('Yes')
else:
    print('No')
