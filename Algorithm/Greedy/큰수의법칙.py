# 그리디 알고리즘 92p문제
# 문제
# 동빈이의 큰수의 법칙은 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰수를 만드는 방법이다.
# 단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
# 예를 들어 순서대로 2, 4, 5, 4, 6으로 이루어진 배열이 있을 때, M이 8이고 K가 3이라고 가정하자.
# 이 경우 특정한 인덱스의 수가 연속해서 세 번까지만 더해질 수 있으므로 큰 수의 법칙에 따른 결과는 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5인 46이 된다.
# 단, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
# 예를 들어 순서대로 3, 4, 3, 4, 3으로 이루어진 배열이 있을 때 M이 7이고 K가 2라고 가정하자.
# 이 경우 두 번째 원소에 해당하는 4와 네 번째 원소에 해당하는 4를 번갈아 두 번씩 더하는 것이 가능하다.
# 결과적으로 4 + 4 + 4 + 4 + 4 + 4 + 4 인 28이 도출된다.

# 배열의크기 N 숫자가 더해지는 횟수 M 연속불가 횟수 K

# 입력 조건
# 1. 첫째 줄에 N(2 <= N <= 1,000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 2. 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다.
# 3. 입력으로 주어지는 K는 항상 M보다 작거나 같다.

# 출력 조건
# 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 입력 예시
# 5 8 3
# 2 4 5 4 6

# 출력 예시
# 46


def bignumber():
    answer = 0
    _, m, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    numbers.sort()

    if m // k > 0:
        answer += numbers[-1] * k * (m // k)
        answer += numbers[-2] * (m % k)
    else:
        answer += numbers[-1] * m

    return answer


print(bignumber())
