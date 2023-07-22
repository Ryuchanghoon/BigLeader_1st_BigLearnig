from collections import deque

def dfs(v):
    stack = [v]
    visited = [False] * (n + 1)
    visited[v] = True

    while stack:
        curr = stack.pop()
        print(curr, end=' ')

        for nxt in reversed(graph[curr]):
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

def bfs(v):
    queue = deque()
    visited = [False] * (n + 1)
    queue.append(v)
    visited[v] = True

    while queue:
        curr = queue.popleft()
        print(curr, end=' ')

        for nxt in graph[curr]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n + 1):
    graph[i].sort()

dfs(v)
print()
bfs(v)