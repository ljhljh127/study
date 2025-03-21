"""
동빈이는 온라인으로 컴퓨터 공학 강의를 듣고 있다. 이 때 각 온라인 강의는 선수 강의가 있을 수 있는데, 선수 강의가 있는 강의는 선수 강의를 먼저 들어야만 해당 강의를 들을 수 있다.
동빈이는 총 N개의 강의를 듣고자 한다. 강의는 1번부터 N번까지의 번호를 가진다. 또한 동시에 여러 개의 강의를 들을 수 있다고 가정한다.
예를 들어, N = 3일 때, 3번 강의의 선수 강의로 1번과 2번 강의가 이씨고, 1번과 2번 강의는 선수 강의가 없다고 하자. 그리고 각 강의에 대하여 강의 시간이 다음과 같다고 하자.

1번 강의: 30시간
2번 강의: 20시간
3번 강의: 40시간

이 경우, 1번 강의를 수강하기까지의 최소 시간은 30시간, 2번 강의를 수강하기까지는 최소 20시간, 3번 강의를 수강하기까지는 최소 70시간이 필요하다.
동빈이가 듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지는 걸리는 최소 시간을 출력하는 프로그램을 작성해라.



입력조건
첫째줄에 동빈이가 듣고자 하는 강의의 수 N(1 <= N <= 500)이 주어진다.
다음 N개의 줄에는 각 강의의 강의시간과 그 강의를 듣기 위해 먼저 들어야 하는 강의들의 번호가 자연수로 주어지며, 각 자연수는 공백으로 구분된다. 이 때 강의 시간은 100,000 이하의 자연수이다.
각 강의 번호는 1부터 N까지로 구성되며, 각 줄은 -1로 끝난다.
출력조건
N개의 강의에 대해 수강하기까지 걸리는 최소 시간을 한 줄에 하나씩 출력한다.

입력 예시

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

출력 예시

10
20
14
18
17
"""

# import sys
# from collections import deque

# n = int(input())
# course_list = []
# # 0은 더미 1부터 시작하게 하기 위한 꼼수
# course_list.append(0)
# for i in range(n):
#     course_list.append(list(map(int, sys.stdin.readline().split())))
# indegree = [0] * (n + 1)
# graph = [[] for i in range(n + 1)]
# cost = [0] * (n + 1)
# for i in range(1, len(course_list)):
#     for j in range(1, len(course_list[i])):
#         # 비용
#         if j == 1:
#             cost[i] = course_list[i][j]
#         # -1 아니면 그래프 append
#         elif course_list[i][j] != -1:
#             graph[course_list[i][j]].append(i)
#             indegree[i] += 1


# def topology_sort():
#     result = []
#     q = deque()
#     for i in range(1, len(indegree)):
#         if indegree[i] == 0:
#             q.append(i)

#     while q:
#         now = q.popleft()
#         result.append(now)
#         for i in graph[now]:
#             indegree[i] -= 1

#             if indegree[i] == 0:
#                 q.append(i)

#     print(result)


# topology_sort()


## 풀지 못한이유 이 이후 시간을 어떻게 다뤄야할지 감이안옴 책참고


import sys
from collections import deque

n = int(input())
course_list = []
# 0은 더미 1부터 시작하게 하기 위한 꼼수
course_list.append(0)
for i in range(n):
    course_list.append(list(map(int, sys.stdin.readline().split())))
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
cost = [0] * (n + 1)
for i in range(1, len(course_list)):
    for j in range(len(course_list[i])):
        # 비용
        if j == 0:
            cost[i] = course_list[i][j]
        # -1 아니면 그래프 append
        elif course_list[i][j] != -1:
            graph[course_list[i][j]].append(i)
            indegree[i] += 1

import copy


def topology_sort():
    result = copy.deepcopy(cost)
    q = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + cost[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(result)


topology_sort()
