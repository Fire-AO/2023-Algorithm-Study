from collections import deque


# 도시들 간의 연결 관계를 확인하고 그래프를 만듭니다.
def make_graph():
    graph = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if connect[i][j] == 1:
                graph[i].append(j)
    return graph


# BFS를 사용하여 동혁이 주어진 순서대로 도시들을 방문할 수 있는지 확인합니다.
def bfs(start, end):
    queue = deque([start])
    visited = [False] * N
    visited[start] = True

    while queue:
        v = queue.popleft()
        if v == end:
            return True
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return False


N = int(input())
M = int(input())

connect = [list(map(int, input().split())) for _ in range(N)]
plan = [int(p) - 1 for p in input().split()]

graph = make_graph()
print(graph)

# 순서대로 도시들을 방문할 수 있는지 확인합니다.
for i in range(M - 1):
    if not bfs(plan[i], plan[i + 1]):
        print('NO')
        break
else:
    print('YES')
