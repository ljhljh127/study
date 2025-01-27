# DFS 기본 구현해보기

graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[6,8],[1,7]]
visited = [False]*9


def dfs(_graph, _visited ,start_node):
    if not _visited[start_node]:
        _visited[start_node] = True
        print(start_node)
        for i in _graph[start_node]:
            if not _visited[i]:
                dfs(_graph,_visited,i)

dfs(graph,visited,1)