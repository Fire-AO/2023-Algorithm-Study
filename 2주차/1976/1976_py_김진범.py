import sys

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

g = [list(map(int, input().split())) for _ in range(n)]

p = list(map(int, input().split()))

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            union(i+1, j+1)

top = find(p[0])
ans = ''
for i in p:
    if find(i) != top:
        ans = 'NO'
        break

if ans == '':
    ans = 'YES'

print(ans)
