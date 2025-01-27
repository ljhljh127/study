# BFS 기본 구현해보기
from collections import deque
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[6,8],[1,7]]

# 재귀로 풀어봄
def recursive_bfs(_graph, _visited, _queue):
    if len(_queue)>0:
        current_node = _queue.popleft()
        print(current_node)
        for i in _graph[current_node]:
            if not _visited[i]:
                _queue.append(i)
                _visited[i] = True
        recursive_bfs(_graph,_visited,_queue)
    else:
        pass # bfs stop!


visited = [False]*9
queue = deque()
visited[1] = True  
queue.append(1)
recursive_bfs(graph,visited,queue)

# 반복문을 사용한다면?
def bfs(_graph, _visited, start_node):
    _queue = deque()
    _visited[start_node]= True
    _queue.append(start_node)
    while _queue:
        current_node = _queue.popleft()
        print(current_node)
        for i in _graph[current_node]:
            if not _visited[i]:
                _queue.append(i)
                _visited[i] = True


visited = [False]*9
bfs(graph,visited,1)