#条件の組み合わせリストを取得
n,m = map(int,input().split())
cnt = 0
jokenList = list()
while cnt < m:
    jokenList.append(list(map(int,input().split())))
    cnt = cnt + 1

#ボールの配置パターンを取得
k = int(input())
cnt = 0
bowlsList = list()
patternList = list()

while cnt < k:
    bowlsList.append(list(map(int,input().split())))
    cnt = cnt + 1

cnt = 0

for i in bowlsList:
  for i2 in i:
    cnt2 = 0
    for j in bowlsList:
      for j2 in j:
        if cnt != cnt2:
          patternList.append([i2,j2])
      cnt2 = cnt2 + 1
  cnt = cnt + 1

#ボールの配置パターンと条件のパターンを比較
cnt = 0
for i in jokenList:
  for j in patternList:
    if set(i) == set(j):
      cnt = cnt + 1
      break

print(cnt)


#回答例
import itertools

N, M = map(int, input().split())
cond = [tuple(map(int, input().split())) for i in range(M)]
K = int(input())
choice = [tuple(map(int, input().split())) for i in range(K)]
ans = 0
for balls in itertools.product(*choice):
    balls = set(balls)
    cnt = sum(A in balls and B in balls for A, B in cond)
    if ans < cnt:
        ans = cnt

print(ans)
