"""
그래프 p298 문제
문제
학교에서 학생들에게 0~N번까지의 번호 부여 처음에는 모든 학생이 서로 다른 팀으로 구분 되어 총 N+1개의 팀이 존재함
선생님은 팁합치기, 같은 팀 여부 확인 연산이 가능하다.
선생님이 M개의 연산을 수행할 수 있을 때 같은 팀 여부확인 연산에 대한 연산 결과를 출력하는 프로그램을 작성해라

입력조건
첫째 줄 N,M이 주어진다. M은 입력으로 주어지는 연산의 개수 N은 1보다 크거나 같고 M은 100,000보다 작거나 같다.
다음 M개의 줄에는 각각의 연산이 주어진다.

팀 합치기 연산은 0 a b 형태로 주어진다. a학생이 속한 팀과 b학생이 속한 팀을 합친다는 의미이다.
같은 팀 여부 확인 연산은 1 a b 형태로 주어진다. a와 b학생이 같은 팀에 속한지 확인하는 연산이다.

같은 팀 여부 확인 연산에 대해 YES or NO 로 출력한다.

입력예시
ex)
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력예시
ex)
NO
NO
YES
"""


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_it_same_team(parent, a, b):
    if find_parent(parent, a) != find_parent(parent, b):
        return "NO"
    else:
        return "YES"


# input
n, m = map(int, input().split())

# 부모 초기화
parent = [0] * (n + 1)
for i in range(n):
    parent[i] = i

# m 만큼 수행하기
for i in range(m):
    op_type, a, b = map(int, input().split())

    if op_type == 0:
        union_parent(parent, a, b)
    elif op_type == 1:
        answer = is_it_same_team(parent, a, b)
        print(answer)
    else:
        print("operation type is wrong!")
        break
