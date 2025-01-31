"""
DFS/BFS 152p 문제
문제
현재 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다. 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다.
이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

입력 조건
첫째 줄에 두 정수 N, M(4≤N,M≤200)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.
또한 시작 칸과 마지막 칸은 항상 1이다.

입력 예시
5 6
101010
111111
000001
111111
111111

출력 예시
10
"""
from collections import deque

def escape_from_maze():
    n,m = map(int,input().split())
    graph = make_maze_map(n, m)
    return bfs(graph, n, m)
    



# 미로 맵 만들기
def make_maze_map(_n, _m):

    maze = []
    for _ in range(_n):
        temp_list = list(map(int,input()))
        if len(temp_list)!= _m:
            print("len error")
            return 
        maze.append(temp_list)
    graph = make_graph(maze, _n, _m)
    return graph


def make_graph(_maze, _n , _m):
    for i in range(_n):
        for j in range(_m):
            node = {}
            adjacent_list = []
            if i-1>=0:
                adjacent_list.append((i-1,j))
            if i+1<_n:
                adjacent_list.append((i+1,j))
            if j-1>=0:
                adjacent_list.append((i,j-1))
            if j+1<_m:
                adjacent_list.append((i,j+1))
            node["adjacent_list"] = adjacent_list

            if _maze[i][j] == 1:
                node["visited"]=False
            if _maze[i][j] == 0:
                node["visited"]=True
            
            node["n"] = i
            node["m"] = j
            
            _maze[i][j] = node
    
    return _maze
            
def bfs(_graph, _n, _m):
    queue = deque()
    _graph[0][0]["visited"] = True
    _graph[0][0]["cost"] = 1
    queue.append(_graph[0][0])
    while queue:
        current_node = queue.popleft()
        if current_node["n"] ==_n-1 and current_node["m"] ==_m-1:
            break

        for adjacent_node in current_node["adjacent_list"]: 
            if not _graph[adjacent_node[0]][adjacent_node[1]]["visited"]:
                _graph[adjacent_node[0]][adjacent_node[1]]["visited"] = True
                _graph[adjacent_node[0]][adjacent_node[1]]["cost"] = current_node["cost"] +1
                queue.append(_graph[adjacent_node[0]][adjacent_node[1]])
                
    return current_node["cost"]

    



print(escape_from_maze())