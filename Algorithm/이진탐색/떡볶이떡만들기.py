"""
이진탐색 p201 문제
문제
떡볶이 떡의 길이는 일정하지 않아서 한 봉지 안에 들어가는 떡의 총길이를 절단기로 잘라서 맞춘다.

절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 H 위 부분이 잘리고, 낮은 떡은 잘리지 않는다.

모든 떡의 잘린 길이만큼 떡을 가져간다.

요청한 총 길이가 M일 때, 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라.

 

입력 조건

첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어진다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
둘째 줄에는 떡의 개별 높이가 주어진다. 떡의 높이의 총합은 항상 M 이상이므로, 손님은 필요한 만큼 떡을 사갈 수 있다. 높이는 10억보다 작거나 같은 양의 정수 또는 0이다.
출력 조건

적어도 M만큼의 떡을 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.
 

입력 예시
4 6
19 15 10 17
출력 예시
15
"""

import sys
import time


def tteokpoki():

    n, m = map(int, sys.stdin.readline().rstrip().split())
    tteok_list = list(map(int, (sys.stdin.readline().rstrip().split())))
    tteok_list.sort()
    return binary_search(0, tteok_list[-1], tteok_list, m)


def binary_search(start, end, array, target):
    answer = -1
    while True:
        mid = (start + end) // 2
        result = is_bigger_than_target(array, target, mid)
        if result:
            start = mid + 1
            if mid > answer:
                answer = mid
        else:
            end = mid - 1

        # for debuging
        print(start, end, mid)
        if start > end:
            break
    return answer


def is_bigger_than_target(_array, _target, _mid):
    result = 0
    for i in _array:
        if i - _mid > 0:
            result += i - _mid
    if result >= _target:
        return True
    else:
        return False


print(tteokpoki())
