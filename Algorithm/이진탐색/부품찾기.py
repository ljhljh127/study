"""
이진탐색 197p문제
부품 찾기
문제 정의
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.

예시
가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.
N = 5
{8, 3, 7, 9, 2}
손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
M = 3
{5, 7, 9}
결과
no yes yes


입력조건
첫째 줄에 정수 N이 주어진다.
N: 1 이상, 1,000,000 이하
둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
셋째 줄에는 정수 M이 주어진다.
M: 1 이상, 100,000 이하
넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.


출력조건
첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.

"""


"""
내가 푼 방식은 슬라이싱을 이용했기 때문에 메모리 낭비가 있음 다음문제 부터는 인덱스 전달 방식으로 해보자
"""

import sys
def find_parts():
    parts_list, request_list = parts_input()
    
    parts_list.sort()

    result = ""
    for i in request_list:
        a = binary_search(i, parts_list)
        result = result + a +" "
    
    print(result)




def parts_input():
    n = int(input())
    parts_input = sys.stdin.readline().rstrip()
    parts_list = list(map(int,parts_input.split()))
    m = int(input())
    request_parts_input = sys.stdin.readline().rstrip()
    request_list = list(map(int,request_parts_input.split()))

    return parts_list, request_list


def binary_search(target, search_list):
    mid_inedex = len(search_list)//2
    mid = search_list[mid_inedex]
    
    if mid == target:
        return "yes"

    elif mid > target:
        if len(search_list) == 1:
            return "no"
        return binary_search(target,search_list[:mid_inedex])
    elif  mid < target:
        if len(search_list) == 1:
            return "no"
        return binary_search(target, search_list[mid_inedex:])




find_parts()