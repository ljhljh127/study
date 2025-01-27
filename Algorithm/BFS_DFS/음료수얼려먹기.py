"""
DFS/BFS 149p 문제
문제 
N x M 크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.   
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.   
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오. 다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

입력 조건

첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N, M <= 1000)
두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
출력 조건

한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
"""

"""
나의 풀이 방법
(0,0) 부터 1이 아닌 0에 대해서 순회하며 DFS 또는 BFS를 수행한다.
그려면 방문된 노드는 1로 처리 될테니 그 다음 1이 아닌 부분에서 반복적으로 탐색을 돌리면 
탐색을 시작하게 되는 횟수가 아이스크림의 개수 일 것이다.
"""
from collections import deque

def frozen_drink():
    n,m=map(int,input().split())
    # 초기 얼음틀 생성
    ice_tray = []
    for _ in range (n):
        temp_list = list(map(int,input()))
        if len(temp_list)>m:
            print("input len error")
            return
        ice_tray.append(temp_list)

    # 그래프 화
    graph = make_graph(ice_tray, n, m)

    # 아이스크림 개수 구하기
    print(calculate_icecream(graph, n, m))

    



def make_graph(_ice_tray, _n, _m):
    for i in range(_n):
        for j in range (_m):
            # 노드 정보를 담을 리스트 선언
            node = []
            # 인접 노드 설정
            adjecent_list = []
            if i -1 >= 0:
                adjecent_list.append((i-1, j))
            if i+1 < _n:
                adjecent_list.append((i+1, j))
            if j-1 >= 0:
                adjecent_list.append((i, j-1))
            if j+1 < _m:
                adjecent_list.append((i, j+1))

            node.append(adjecent_list)

            # 방문 여부(1) 설정
            if _ice_tray[i][j] == 1:
                node.append(True)
            elif _ice_tray[i][j] == 0:
                node.append(False)
            else: raise ValueError

            _ice_tray[i][j] = node
    return _ice_tray


def calculate_icecream(_graph, _n, _m):
    icecream_cnt = 0
    # graph[i][j][0] == 인접노드 정보
    # graph[i][j][1] == 방문여부
    for i in range (_n):
        for j in range (_m):
            current_node = _graph[i][j]
            if current_node[1] is not True:
                icecream_cnt +=1
                current_node[1] = True
                queue = deque()
                queue.append(current_node[0])
                while queue:
                    obj = queue.popleft()
                    for adjn in obj:
                        if _graph[adjn[0]][adjn[1]][1] is not True:
                            _graph[adjn[0]][adjn[1]][1] = True
                            queue.append(_graph[adjn[0]][adjn[1]][0])
    return icecream_cnt
                        

frozen_drink()