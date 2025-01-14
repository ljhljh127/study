"""
그리디 알고리즘 87p 문제
문제
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원,
100원, 50원, 10원 짜리가 무한이 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러
줘야 할 동전의 최소 개수를 구하라. 단. 거슬러 줘야할 돈은 항상 N의 배수이다.
"""


def change(money: int) -> int:
    result = 0
    if money > 0:
        changes = [500, 100, 50, 10]
        for change in changes:
            result = result + money // change
            money = money % change
    return result


answer = change(3520)
print(answer)
