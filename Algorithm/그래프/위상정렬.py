from collections import deque

"""
먼저 초기화 과정이다. 그래프를 초기화하고 해당 노드로 들어가는 항목들을 기입한다.
graph[a].append(b)는 a to b 로 이동하는 방향이며
따라서 b로 들어가는 하위 노드의 개수를 늘린다.
"""
v, e = map(int, input().split())
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(result)


topology_sort()
