import sys

# 입력받기
n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)  # 정수형 무제한

# 그래프 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신 비용은 0으로
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = c

# k가 가장 바깥이여야 업데이트된 k값을 쓸수있음
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
