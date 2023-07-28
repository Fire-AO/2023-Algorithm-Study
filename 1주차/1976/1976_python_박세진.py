import sys
"""
Union-Find 문제 M값때문에 헷갈렸다.
결론적으로는 의미 없는 변수 값이었다.
"""
def find(x): # 재귀로 루트 노드 탐색
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y): # 노드 합치기
    rootx = find(x)
    rooty = find(y)
    if rootx != rooty:
        parent[rooty] = rootx

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

parent = list(range(n))

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
plan = [x-1 for x in plan]

root = find(plan[0])
res = 'YES'

for city in plan:
    if find(city) != root:
        res = 'NO'
print(res)