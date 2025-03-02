import sys

# n: 회사의 개수 m: 경로의 개수
n, m = map(int, sys.stdin.readline().rstrip().split())

# 최대값 설정
INF = int(1e9)

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신은 0으로
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 연결노드 설정
for _ in range(m):
    o, p = map(int, sys.stdin.readline().rstrip().split())
    graph[o][p] = 1
    graph[p][o] = 1

# X와 K값 받기 각각 회사
x, k = map(int, sys.stdin.readline().rstrip().split())

# 플루이드
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 문제는 1번회사에서 K번회사 To X번회사 따라서 1 To K + 1 To X
answer = graph[1][k] + graph[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)
