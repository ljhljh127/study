import sys
import heapq

# n:도시의 개수 m: 통로의 개수 c:송신도시
n, m, c = map(int, sys.stdin.readline().rstrip().split())

# 최대값 설정
INF = int(1e9)

# graph 초기화
graph = [[] for i in range(n + 1)]

# distance 리스트 초기화
distance = [INF] * (n + 1)
for i in range(m):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    graph[x].append((y, z))


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


def make_answer():
    count = 0
    max_value = 0
    for i in distance:
        if i < INF and i > 0:
            print(i)
            count += 1
            max_value = max(max_value, i)
    return count, max_value


djikstra(c)
print(make_answer())
