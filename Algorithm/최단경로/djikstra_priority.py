import sys

# 입력받기
n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)  # 정수형 무제한
import heapq

# 그래프 초기화 시작
"""
그래프 각 노드별 연결정보를 담기위한 리스트
ex)[ [] [] [] [] ]
각각 0번 1번 2번 3번 인덱스의 연결된 노드 표기용
"""
graph = [[] for i in range(n + 1)]
print("initialize graph")
print(graph)

distance = [INF] * (n + 1)  # 최단거리 리스트 모두 무제한으로 초기화
print(distance)

# 그래프 만들기 시작

# 모든 간선정보 입력받기
# a노드 to b노드 비용=c
# 예시 [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))

print(graph)


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        # 현재 노드의 거리가 최초 거리보다 작아졌다면 이미 처리한거로 간주하고 패스
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


djikstra(1)
print(distance)
