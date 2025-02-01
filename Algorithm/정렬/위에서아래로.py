"""
정렬 178p 문제
문제
수열을 큰 수부터 작은 수로 내림차순 정렬하시오

입력조건
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어짐(1<= N <= 500)
둘째 줄부토 N+1번째 줄 까지 N개의 수가 입력됨 수으 ㅣ범위는 1이상 100,000 이하의 자연수이다.

츨력조건
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다 동일한 수의 순서는 자유
"""
def uptodown():
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))

    array.sort(reverse=True)

    for i in array:
        print(i,end =' ')

uptodown()