
"""
구현 115p 문제
문제
행복 왕국의 왕실 정원은 체스판과 같은 8 x 8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서있다. 나이트는 매우 충성스러운 신하로서 매일 무술을 연마한다. 나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.   
나이트는 특정 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
이처럼 8 x 8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하라.   
왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a 부터 h로 표현한다
예를 들어 만약 나이트가 a1에 있을 때 이동할 수 있는 경우의 수는 다음과 같은 2가지이다.   
a1의 위치는 좌표 평면에서 구석의 위치에 해당하며 나이트는 정원의 밖으로는 나갈 수 없기 때문이다.
오른쪽으로는 두 칸 이동 후 아래로 한 칸 이동하기 (c2)
아래로 두 칸 이동 후 오른쪽으로 한 칸 이동하기 (b3)
또 다른 예로 나이트가 c2에 위치해 있다면 나이트가 이동할 수 있는 경우의 수는 6가지이다. 이건 직접 계산해보시오.

<입력 조건>
첫째 줄에 8 X 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 문자열이 입련된다. 입력 문자는 a1처럼 열과 행으로 이뤄진다.

<출력 조건>
첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.
"""

def knightofkingdom():
    alphabets=["a","b","c","d","e","f","g","h"]

    posistion=input()
    c,r = posistion
    startc=alphabet_to_index(alphabets,c)
    startr=int(r)
    return move_knight(startc,startr,len(alphabets))

def alphabet_to_index(_alphabets,target):
    for i in range(len(_alphabets)):
        if _alphabets[i]== target:
            return i+1


def move_knight(_startc, _startr, alphabetslen):
    answer = 0
    if _startc-2 >0:
        if _startr +1 <=alphabetslen: 
            answer+=1
        if _startr-1 >=1:
            answer+=1
    if _startc+2 <=alphabetslen:
        if _startr +1 <=alphabetslen:
            answer+=1
        if _startr-1 >=1:
            answer +=1
    if _startr-2 >0:
        if _startc +1 <=alphabetslen:
            answer+=1
        if _startc-1 >=1:
            answer+=1
    if _startr+2 <=alphabetslen:
        if _startc +1 <=alphabetslen:
            answer+=1
        if _startc-1 >=1:
            answer+=1
    return answer




print(knightofkingdom())