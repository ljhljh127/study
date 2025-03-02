import sys

# 입력받기
n, m = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)  # 정수형 무제한
start = int(input())

# 그래프 초기화 시작
"""
그래프 각 노드별 연결정보를 담기위한 리스트
ex)[ [] [] [] [] ]
각각 0번 1번 2번 3번 인덱스의 연결된 노드 표기용
"""
graph = [[] for i in range(n + 1)]
print("initialize graph")
print(graph)

visited = [False] * (n + 1)  # 방문여부를 담기위한 리스트
distance = [INF] * (n + 1)  # 최단거리 리스트 모두 무제한으로 초기화
print(distance)

# 그래프 만들기 시작

# 모든 간선정보 입력받기
# a노드 to b노드 비용=c
# 예시 [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], [(3, 3), (5, 1)], [(3, 1), (6, 2)], []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


# 다익스라 알고리즘 적용
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        # i[0] == 노드 , i[1] == 비용
        # 즉 아래는 출발 노드로부터 각 노드까지의 비용을 설정해주는 것
        distance[i[0]] = i[1]
    for j in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for k in graph[now]:
            cost = distance[now] + k[1]

            if cost < distance[k[0]]:
                distance[k[0]] = cost


# 방문 안한 노드에서 가장 최단거리가 짧은 노드 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


dijkstra(1)
print(distance)
