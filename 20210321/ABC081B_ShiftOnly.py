def amariCheck(A):
    for i in A:
        if i == 0:
            return False
    
    A = list(map(lambda x: x%2,A))
    for i in A:
        if i != 0:
            return False
    return True

N = int(input())
A = list(map(int,input().split()))
ans = 0

while True:
    if amariCheck(A):
        ans+=1
    else:
        break
    A = list(map(lambda x: x/2,A))

print(ans)
