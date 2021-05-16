N = int(input())
d = list()
tmp = 101
cnt = 0

for i in range(N):
    d.append(int(input()))

for i in range(N):
    m = max(d)
    idx = d.index(m)
    if m < tmp:
        cnt += 1
        tmp = m
    del d[idx]

print(cnt)