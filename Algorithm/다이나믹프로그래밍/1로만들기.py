"""
다이나믹 프로그래밍 217p문제
문제
정수 X가 주어질때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1) X가 5로 나누어떨어지면, 5로 나눈다.
2) X가 3으로 나누어 떨어지면, 3으로 나눈다.
3) X가 2로 나누어 떨어지면, 2로 나눈다.
4) X에서 1을 뺀다.

정수 X가 주어졌을때, 연산 4개를 적절히 사용해서 1을 만들어야한다. 이 연산을 사용하는 횟수의 최솟값을 출력해라.

X = 26일 경우
1. 26 - 1 = 25

2. 25 /5 = 5

3. 5 / 5 = 1

출력값 : 3
"""

# DP로 접근
cache = [-1] *30001
def make_1(x):
    if x == 1:
        return 0
    if cache[x] != -1:
        return cache[x]
    count = 30001

    if x % 5 == 0:
        count = min(count, make_1(x // 5) + 1)
    if x % 3 == 0:
        count = min(count, make_1(x // 3) + 1)
    if x % 2 == 0:
        count = min(count, make_1(x // 2) + 1)
    
    count = min(count, make_1(x-1) +1)
    cache[x] = count

    return count    

start = int(input())
print(make_1(start))


count = 0
# 탐욕으로 접근하여 틀림
def make_1(x):
    global count
    if x == 1:
        return count
    if x % 5 <= 1:
        count +=1
        minus_count = x%5
        count += minus_count
        x = (x - minus_count) // 5
        return make_1(x)
    
    if x % 3 <= 1:
        count +=1
        minus_count = x%3
        count += minus_count
        x = (x - minus_count) // 3
        return make_1(x)
    
    if x % 2 <= 1:
        count +=1
        minus_count = x%2
        count += minus_count
        x = (x - minus_count) // 2
        return make_1(x)


start = int(input())
print(make_1(start))