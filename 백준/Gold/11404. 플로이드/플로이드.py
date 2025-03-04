import sys
input = sys.stdin.readline

n = int(input())  # 도시의 수
m = int(input())  # 버스의 수

INF = float("inf")
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    src, dst, weight = map(int, input().split())
    graph[src][dst] = min(graph[src][dst], weight)

for k in range(1, n + 1):
    graph[k][k] = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0 , end=" ") #부럽다
        else:
            print(graph[i][j], end=" ")
    print()
