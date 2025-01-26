"""
구현 118p 문제
문제
게임 캐릭터가 맵 안에서 움직이는 시스템이 있다. 캐릭터가 있는 장소는 1 X 1 크기의 정사각형으로 이뤄진 N X M 크기의 직사각형으로, 각각의 칸은 육지 또는 바다이다.   
캐릭터는 동서남북 중 한 곳을 바라본다. 맵의 각 칸은 (A, B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수이다.   
캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다. 움직임을 위한 매뉴얼은 다음과 같다.

현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 갈 곳을 정한다.
캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오

[입력조건]
* 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력(3<=N, M<=50)
* 둘째 줄에 게임 캐릭터가 있는 칸의 좌표와 바라보는 방향 d 가 각각 서로 공백으로 구분하여 주어짐 방향 d의 값으로는
0 : 북
1 : 동
2 : 남
3 : 서
* 셋째 줄부터 맵이 육지인지 바다인지 정보 주어짐 
육지 : 0
바다 : 1

 

처음 캐릭터가 위치한 칸은 항상 육지

이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
"""

def game_develop():
    n,m= map(int,input().split())
    a,b,d = map(int,input().split())
    count = 1
    gamemap =[]
    for _ in range(n):
        temp_list=list(map(int,input().split()))
        if len(temp_list)!=m:
            return ValueError("input list len error")
        gamemap.append(temp_list)
    
    while True:
        d=first_step(d)
        gamemap,count,a,b = second_step(a,b,d,gamemap,count)
        if third_step(gamemap,a,b):
            break
    return count

# 방향 회전
def first_step(_d):
    if _d -1 == -1:
        return 3
    else:
        return _d-1

# 내가 갈 수 있는지 판단하고 갈 수 있다면 이동 후 방문처리   
def second_step(_a, _b, _d, _gamemap, count):
    if _d ==0:
        if _gamemap[_a-1][_b] == 0:
            _gamemap[_a-1][_b] = 1
            count +=1
            return _gamemap, count, _a-1,_b
    if _d==1:
        if _gamemap[_a][_b+1]==0:
            _gamemap[_a][_b+1] = 1
            count +=1
            return _gamemap, count, _a, _b+1
    if _d==2:
        if _gamemap[_a+1][_b]==0:
            _gamemap[_a+1][_b] = 1
            count +=1
            return _gamemap, count, _a+1, _b
    if _d==3:
        if _gamemap[_a][_b-1]==0:
            _gamemap[_a][_b-1] =1
            count +=1
            return _gamemap, count, _a, _b-1
    return _gamemap, count, _a,_b

# 끝내기 검증 내 4방면이 1 로 둘러쌓여있는지
def third_step(_gamemap, _a, _b):
    if _gamemap[_a-1][_b] == 1 and _gamemap[_a+1][_b] == 1 and _gamemap[_a][_b-1] == 1 and _gamemap[_a][_b+1] == 1:
        return True
    return False

print(game_develop())